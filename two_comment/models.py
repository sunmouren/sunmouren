from django.db import models
from django.conf import settings

"""
    这里可以直接在settings里设置要评论的条目和所属作者
    比如我的项目里的是：
    # 自定义用户model
    AUTH_USER_MODEL = 'users.user'
    # two comments settings
    COMMENT_ENTRY_MODEL = 'forum.post'
"""


class Comment(models.Model):
    entry = models.ForeignKey(settings.COMMENT_ENTRY_MODEL, related_name='entry_comments')
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_comments', blank=True, null=True)
    user_favour = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='comment_favour', blank=True)
    submit_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['submit_date']

    def __str__(self):
        return '%s 评论了 %s' % (self.author.username, self.entry)


class CommentReply(models.Model):
    comment = models.ForeignKey(Comment, related_name='comment_reply', blank=True, null=True)
    content = models.TextField()
    author_from = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_reply', blank=True, null=True)
    author_to = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    submit_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['submit_date']

    def __str__(self):
        return '%s @ %s ' % (self.author_from.username, self.author_to.username)
