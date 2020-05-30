from django import forms
 
from .models import Post


class PostSubmitForm(forms.ModelForm):
    '''
    ModelForm that provides security when creating new `Post` object
    '''

    body = forms.CharField(label=None, required=True, max_length=160, widget=forms.TextInput(
        attrs={
            'autocorrect': 'off',
            'autocomplete': 'off',
            'autocapitalize': 'off',
            'id': 'submision-body',
            'name': 'submision-body',
            'placeholder': 'have an epic cheat day',
        }
    ))
    city = forms.CharField(label=None, required=True, max_length=300, widget=forms.TextInput(
        attrs={
            'autocorrect': 'off',
            'autocomplete': 'off',
            'autocapitalize': 'off',
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