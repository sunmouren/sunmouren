from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(max_length=128, blank=True, verbose_name='标题', default='无标题')
    body = models.TextField(verbose_name='内容')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='forum_posts')
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='posts_liked',
                                       blank=True)
    total_like = models.PositiveIntegerField(default=0, db_index=True)
    view_count = models.PositiveIntegerField(default=0, verbose_name='查看次数')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '文章'
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum:post_detail', args=[self.id])

    def get_summary(self):
        return self.body[:60]

    def view_count_increase(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])