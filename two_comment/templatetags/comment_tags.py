from django import template

from ..forms import CommentForm, ReplyForm

register = template.Library()


@register.simple_tag
def get_comment_list(entry):
    return entry.entry_comments.all()


@register.simple_tag
def get_reply_list(comment):
    return comment.comment_reply.all()


@register.simple_tag
def get_comment_form():
    return CommentForm()


@register.simple_tag
def get_reply_form():
    return ReplyForm()



