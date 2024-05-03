from django import forms


class MovieSearchForm(forms.Form):
    supplied_movie_name = forms.CharField(label='Movie Name', max_length=100)
