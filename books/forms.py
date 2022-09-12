from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Join the discussion...',
        'rows': '4',
    }))
    
    class Meta:
        model = Comment
        fields = ('text', )
