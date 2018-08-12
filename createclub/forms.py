from django import forms

from .models import MovieClub

class MovieClubForm(forms.ModelForm):

    class Meta:
        model = MovieClub
        fields = ('name', 'privacy',)