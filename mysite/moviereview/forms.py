from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class MovieSearchForm(forms.Form):
    supplied_movie_name = forms.CharField(label='Movie Name', max_length=100)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
