from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from actions.utils import create_action
from actions.models import Action

from .forms import UserDetailForm, RegisterForm
from .models import User, Contact


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('forum:post_list'))


def register(request):
    if request.method != 'POST':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('users:edit_profile'))

    context = {'form': form}
    return render(request, 'users/register.html', context)


def profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'users/profile.html', {'user': user})


@login_required
def edit_profile(request):
    messages = []
    if request.method == 'POST':
        form = UserDetailForm(instance=request.user,
                              data=request.POST,
                              files=request.FILES)
        if form.is_valid():
            form.save()
            messages.append('资料更新成功!')

    form = UserDetailForm(instance=request.user)
    context = {'form': form, 'messages': messages}
    return render(request, 'users/edit_profile.html', context)


@require_POST
@login_required
def user_follow(request):
    """
    因为使用了一个定制中介模型（intermediate model）给用户的多对多关系，
    所以ManyToManyField管理器默认的add()和remove()方法将不可用。
    只能使用中介Contact模型（model）来创建或删除用户关系。
    """
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user,
                                              user_to=user)
                create_action(request.user, '关注了', user)
            else:
                Contact.objects.filter(user_from=request.user,
                                       user_to=user).delete()
            return JsonResponse({'msg': 'ok'})
        except user.DoesNotExist:
            return JsonResponse({'msg': 'ko'})
    return JsonResponse({'msg': 'ko'})


@login_required
def following_actions(request):
    actions = Action.objects.exclude(user=request.user)
    following_ids = request.user.following.values_list('id', flat=True)
    if following_ids:
        actions = actions.filter(user_id__in=following_ids).select_related('user').prefetch_related('target')
    else:
        actions = None
    return render(request,
                  'users/following_actions.html',
                  {'actions': actions})