from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from django.core.urlresolvers import reverse


class Contact(models.Model):
    """
    当你使用了一个中介模型（intermediate model）给多对多关系，
    一些关系管理器的方法将不可用，例如：add()，create()以及remove()。
    你需要创建或删除中介模型（intermediate model）的实例来代替。
    """
    user_from = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  related_name='rel_from_set')
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} 关注了 {}'.format(self.user_from, self.user_to)


class User(AbstractUser):
    nickname = models.CharField(max_length=30, blank=True, null=True, verbose_name='昵称')
    signature = models.CharField(max_length=128, blank=True, null=True, verbose_name='座右铭')
    following = models.ManyToManyField('self',
                                       through=Contact,
                                       related_name='followers',
                                       symmetrical=False)
    avatar = ProcessedImageField(upload_to='avatar',
                                 default='avatar/default.png',
                                 verbose_name='头像',
                                 processors=[ResizeToFill(85, 85)])

    class Meta(AbstractUser.Meta):
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if len(self.avatar.name.split('/')) == 1:
            self.avatar.name = self.username + '/' + self.avatar.name
        super(User, self).save()

    def get_absolute_url(self):
        return reverse('users:profile', args=[self.id])





