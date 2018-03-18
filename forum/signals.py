from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Post


@receiver(m2m_changed, sender=Post.user_like.through)
def user_like_changed(sender, instance, **kwargs):
    instance.total_like = instance.user_like.count()
    instance.save()