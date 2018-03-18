from django import template


register = template.Library()


@register.filter(name='remove_markdown')
def remove_markdown(value):
    """
    主要是为了让默认概要去掉markdown语法。
    通过定义常用的markdown语法字符来进行替换成''
    """
    for str in [">", "#", "[", "]", "!", "-"]:
        value = value.replace(str, '')
    return value