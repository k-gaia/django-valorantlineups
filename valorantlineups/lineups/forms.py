from dataclasses import field
from re import T
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # specify which model this form respresents, inherit from
    # built in Django UserCreationForm
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        
        return user
