from django import forms

from lineups.models import Lineup

class NewLineupForm(forms.ModelForm):

    class Meta:
        model = Lineup
        fields = ('character', 'ability', 'name', 'xPos', 'yPos',)
