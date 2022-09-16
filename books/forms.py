from django import forms

from .models import Comment, ReplyToComment


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Join the discussion...',
        'rows': '4',
    }))
    
    class Meta:
        model = Comment
        fields = ('text', 'recommend', )


class ReplyToCommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'reply here...',
        'rows': '2',
    }))

    class Meta:
        model = ReplyToComment
        fields = ('text', )
