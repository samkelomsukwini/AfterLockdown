from django import forms
 
from .models import Post


class PostSubmitForm(forms.ModelForm):
    '''
    ModelForm that provides security when creating new `Post` object
    '''

    body = forms.CharField(label='What is your post-quarantine aspiration?', required=True, max_length=160, widget=forms.TextInput(
        attrs={
            'autocorrect': 'off',
            'autocomplete': 'off',
            'autocapitalize': 'off',
            'id': 'submision-body',
            'title': 'What is your post-quarantine aspiration?',
            'name': 'submision-body',
            'placeholder': 'have an epic cheat day',
        }
    ))
    city = forms.CharField(label='Where are you?', required=True, max_length=300, widget=forms.TextInput(
        attrs={
            'autocorrect': 'off',
            'autocomplete': 'off',
            'autocapitalize': 'off',
            'title': 'Where are you?',
            'id': 'city',
            'name': 'city',
            'placeholder': 'Your city',
        }
    ))
    class Meta:
        model = Post
        fields = (
            'body',
            'city',
        )