from django import forms

from .models import Comment, CommentReply


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': ''}
        widgets = {'content': forms.Textarea(attrs={'rows': 3, 'placeholder': '写下你的评论...'})}


class ReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = ['content']
        labels = {'content': ''}
        widgets = {'content': forms.Textarea(attrs={'rows': 3, 'placeholder': '写下你的评论...'})}