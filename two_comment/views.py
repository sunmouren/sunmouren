from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.conf import settings
from django.apps import apps

from .models import Comment
from .forms import CommentForm, ReplyForm

from . import signals

"""
    这里解释下需要导入相关内容：
    login_required: 用来判断请求对象是否登入
    request_POST: 只能发起POST请求
    settings +  apps : 获取settings中设置的评论Entry，和所需User

"""


@login_required
@ require_POST
def submit_comment(request):
    """
    提交评论
    """
    entry_id = request.POST.get('id')
    app_model = settings.COMMENT_ENTRY_MODEL.split('.')
    Entry = apps.get_model(*app_model)
    if entry_id:
        try:
            entry = Entry.objects.get(id=entry_id)
            form = CommentForm(data=request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.entry = entry
                new_comment.author = request.user
                new_comment.save()
                new_comment_location = '#comment-' + str(new_comment.id)
                return JsonResponse({'status': 'ok', 'new_comment_location': new_comment_location})
        except Entry.DoesNotExist:
            return JsonResponse({'status': 'ko'})
    return JsonResponse({'status': 'ko'})


@login_required
@ require_POST
def submit_reply(request):
    """
    提交回复
    """
    comment_id = request.POST.get('comment_id')
    author_to_id = request.POST.get('author_to_id')
    app_model = settings.AUTH_USER_MODEL.split('.')
    User = apps.get_model(*app_model)
    if comment_id and author_to_id:
        try:
            comment = Comment.objects.get(id=comment_id)
            author_to = User.objects.get(id=author_to_id)
            form = ReplyForm(data=request.POST)
            if form.is_valid():
                new_reply = form.save(commit=False)
                new_reply.comment = comment
                new_reply.author_from = request.user
                new_reply.author_to = author_to
                new_reply.save()
                return JsonResponse({'status': 'ok'})
        except Comment.DoesNotExist or User.DoesNotExist:
            return JsonResponse({'status': 'ko'})
    return JsonResponse({'status': 'ko'})


@login_required
@require_POST
def submit_favour(request):
    """
    提交点赞
    """
    comment_id = request.POST.get('id')
    action = request.POST.get('action')
    if comment_id and action:
        try:
            comment = Comment.objects.get(id=comment_id)
            if action == 'favour':
                comment.user_favour.add(request.user)
            else:
                comment.user_favour.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Comment.DoesNotExist:
            return JsonResponse({'status': 'ko'})
    return JsonResponse({'status': 'ko'})