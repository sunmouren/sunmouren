from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_POST

from actions.utils import create_action

from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 8)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')
        posts = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'forum/post/list_ajax.html',
                      {'posts': posts})
    return render(request,
                  'forum/post/list.html',
                  {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.view_count_increase()
    return render(request,
                  'forum/post/detail.html',
                  {'post': post})


@login_required
def new_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            create_action(request.user, 'new_post', new_post)
            return HttpResponseRedirect(reverse('forum:post_list'))
    return render(request, 'forum/post/new.html', {'form': form})


@login_required
@require_POST
def post_like(request):
    post_id = request.POST.get('id')
    action = request.POST.get('action')
    if post_id and action:
        try:
            post = Post.objects.get(id=post_id)
            if action == 'like':
                post.user_like.add(request.user)
                create_action(request.user, 'like', post)
            else:
                post.user_like.remove(request.user)
            return JsonResponse({'msg': 'ok'})
        except Post.DoesNotExist:
            return JsonResponse({'msg': 'ko'})
    return JsonResponse({'msg': 'ko'})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile', args=[post.author.id]))

    context = {'post': post, 'form': form}
    return render(request, 'forum/post/edit_post.html', context)


