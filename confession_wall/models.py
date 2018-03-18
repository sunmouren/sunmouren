from django.db import models
from django.core.urlresolvers import reverse


class Confession(models.Model):
    """
    表白墙，提供To和找某人的选项
    """
    TO = 'To'
    FIND = 'Find'
    MOTION_CHOICES = (
        (TO, 'To'),
        (FIND, 'Find')
    )
    motion = models.CharField(max_length=5, choices=MOTION_CHOICES, default=TO)
    name = models.CharField(max_length=10, blank=True, null=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('confession_wall:confession_detail', args=[self.id])


class BaseComment(models.Model):
    """
    抽象出评论和回复的共同字段
    """
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['created']

    def __str__(self):
        return self.content


class Comment(BaseComment):
    confession = models.ForeignKey(Confession, related_name='comments')


class Reply(BaseComment):
    comment = models.ForeignKey(Comment, related_name='replies')


