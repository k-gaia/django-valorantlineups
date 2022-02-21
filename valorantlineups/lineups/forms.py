from django import forms

from lineups.models import ChildLineup, Lineup

class NewLineupForm(forms.ModelForm):

    class Meta:
        model = Lineup
        fields = ('character', 'ability', 'name', 'xPos', 'yPos', 'map',
        'childPinAmount', 'childPinIds', 'isAttacking', 'rating', 'createdOn',
        'author',     
        )

class NewChildLineupForm(forms.ModelForm):

    class Meta: 
        model = ChildLineup
        fields = ('name', 'content', 'xPos', 'yPos',)
