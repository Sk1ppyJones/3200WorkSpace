from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'  # ['username', 'rating', 'review_text']
        # exclude = ['username']
        labels = {
            'username': 'Your Name',
            'rating': 'Your Rating',
            'review_text': 'Your Review'
        }
        # max_length = {
        #     'username': 100,
        #     'review_text': 200
        # }
        # min_value = {
        #     'rating': 1
        # }
        # max_value = {
        #     'rating': 5
        # }
        error_messages = {
            'username': {
                'required': 'Please enter your name.',
                'max_length': 'Name cannot exceed 100 characters.'
            },
            'rating': {
                'required': 'Please enter a rating.',
                'min_value': 'Rating must be at least 1.',
                'max_value': 'Rating cannot exceed 5.'
            },
            'review_text': {
                'required': 'Please enter your review.',
                'max_length': 'Review cannot exceed 200 characters.'
            }
        }

# class ReviewForm(forms.Form):
#     username = forms.CharField(label='Your Name', max_length=100, error_messages={
#         'required': 'Please enter your name.',
#         'max_length': 'Name cannot exceed 100 characters.'
#     })
#     rating = forms.IntegerField(label='Your Rating', min_value=1, max_value=5, error_messages={
#         'required': 'Please enter a rating.',
#         'min_value': 'Rating must be at least 1.',
#         'max_value': 'Rating cannot exceed 5.'
#     })
#     review_text = forms.CharField(label='Your Review', widget=forms.Textarea, max_length=200, error_messages={
#         'required': 'Please enter your review.',
#         'max_length': 'Review cannot exceed 200 characters.'
#     })
