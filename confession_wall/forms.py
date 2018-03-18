from django import forms

from .models import Comment, Reply, Confession


class ConfessionForm(forms.ModelForm):
    class Meta:
        model = Confession
        fields = ['motion', 'name', 'content']
        labels = {'content': '', 'motion': '', 'name': ''}
        widgets = {'name': forms.TextInput(attrs={'placeholder': '这里写下给谁', 'class': 'confession-name'}),
                   'content': forms.Textarea(attrs={'rows': 3, 'placeholder': '写下你的表白,万一实现了呢'})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': ''}
        widgets = {'content': forms.Textarea(attrs={'rows': 3, 'placeholder': '写下你的评论...'})}


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        labels = {'content': ''}
        widgets = {'content': forms.Textarea(attrs={'rows': 3, 'placeholder': '写下你的评论...'})}

