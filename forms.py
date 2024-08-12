from django import forms
from .models import PostBox, Comment


class PostBoxForm(forms.ModelForm):
    class Meta:
        model = PostBox
        fields = ['header', 'body']
        widgets = {
            # Adjust the size as needed
            'body': forms.Textarea(attrs={'rows': 10, 'cols': 80}),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
