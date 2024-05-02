from django import forms


class MovieIDForm(forms.Form):
    imdb_id = forms.CharField(label='IMDb ID', max_length=20)
