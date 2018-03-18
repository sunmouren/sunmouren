from django.contrib import admin
from .models import Confession, Comment, Reply


@admin.register(Confession)
class ConfessionAdmin(admin.ModelAdmin):
    list_display = ['content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['confession', 'content']


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['comment', 'content']


