from django.db.models.signals import post_save


from notifications.signals import notify

from two_comment.models import Comment, CommentReply
from users.models import User


def comment_handler(sender, instance, created, **kwargs):
    # 避免自己接收自己评论通知
    recipients = User.objects.exclude(id=instance.author.id)
    if instance.entry.author in recipients:
        notify.send(instance.author, recipient=instance.entry.author,
                    verb='评论了你',
                    action_object=instance,
                    target=instance.entry,
                    description=instance.content)

post_save.connect(comment_handler, sender=Comment)


def reply_handler(sender, instance, created, **kwargs):
    # 避免自己接收自己回复通知
    recipients = User.objects.exclude(id=instance.author_from.id)
    if instance.author_to in recipients:
        notify.send(instance.author_from, recipient=instance.author_to,
                    verb='回复了你',
                    action_object=instance,
                    target=instance.comment,
                    description=instance.content)

post_save.connect(reply_handler, sender=CommentReply)