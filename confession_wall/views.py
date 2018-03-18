from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from .models import Confession, Comment
from .forms import CommentForm, ReplyForm, ConfessionForm


def get_confessions(request):
    confessions = Confession.objects.all()
    return render(request, 'confession_wall/confession_wall_list.html', {'confessions': confessions})


@login_required
@ require_POST
def new_confession(request):
    form = ConfessionForm(data=request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'ko'})


def confession_detail(request, confession_id):
    confession = get_object_or_404(Confession, id=confession_id)
    return render(request, 'confession_wall/confession_detail.html', {'confession': confession})


@login_required
@ require_POST
def submit_confession_comment(request):
    confession_id = request.POST.get('id')
    if confession_id:
        try:
            confession = Confession.objects.get(id=confession_id)
            form = CommentForm(data=request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.confession = confession
                new_comment.save()
                new_comment_location = '#comment-' + str(new_comment.id)
                return JsonResponse({'status': 'ok', 'new_comment_location': new_comment_location})
        except Confession.DoesNotExist:
            return JsonResponse({'status': 'ko'})
    return JsonResponse({'status': 'ko'})


@login_required
@ require_POST
def submit_reply_comment(request):
    comment_id = request.POST.get('comment_id')
    if comment_id:
        try:
            comment = Comment.objects.get(id=comment_id)
            form = ReplyForm(data=request.POST)
            if form.is_valid():
                new_reply = form.save(commit=False)
                new_reply.comment = comment
                new_reply.save()
                return JsonResponse({'status': 'ok'})
        except Comment.DoesNotExist:
            return JsonResponse({'status': 'ko'})
    return JsonResponse({'status': 'ko'})