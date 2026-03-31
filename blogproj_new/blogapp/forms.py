from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'user_email', 'text']
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }