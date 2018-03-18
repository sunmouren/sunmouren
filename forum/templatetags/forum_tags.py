from django import template

from actions.models import Action


from ..models import Post

register = template.Library()


@register.simple_tag
def get_most_popular_post(num=5):
    return Post.objects.order_by('-total_like')[:num]


@register.filter(name='remove_markdown')
def remove_markdown(value):
    """
    主要是为了让默认概要去掉markdown语法。
    通过定义常用的markdown语法字符来进行替换成''
    """
    return value.replace('>', '')


@register.simple_tag
def get_user_posts(user):
    return Post.objects.filter(author=user)


@register.simple_tag
def get_user_action(user):
    return Action.objects.filter(user=user)


@register.simple_tag
def get_user_followings(user):
    return user.following.all()


@register.simple_tag
def get_user_followings_count(user):
    return user.following.count()


@register.simple_tag
def get_user_followers(user):
    return user.followers.all()


@register.simple_tag
def get_user_followers_count(user):
    return user.followers.count()


