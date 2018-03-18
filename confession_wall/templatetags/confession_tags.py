from django import template

from ..forms import CommentForm, ReplyForm, ConfessionForm

register = template.Library()


@register.simple_tag
def get_comment_list(entry):
    return entry.comments.all()


@register.simple_tag
def get_reply_list(comment):
    return comment.replies.all()


@register.simple_tag
def get_new_confession_form():
    return ConfessionForm()


@register.simple_tag
def get_comment_form():
    return CommentForm()


@register.simple_tag
def get_reply_form():
    return ReplyForm()



