from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class CustomUserCreationForm(UserCreationForm): #custom user creation form

    email = forms.EmailField(required=True) 

    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #shown fields

class ProfileUpdateForm(forms.ModelForm): #Update profile form
    email = forms.EmailField()        

    class Meta: 
        model = Profile 
        fields = ['bio', 'profile_picture']# fields to show in the form

    def save(self, commit=True): #save method to update user email and profile
        profile = super().save(commit=False) # get profile instance
        profile.user.email = self.cleaned_data['email'] 
        if commit: 
            profile.user.save() 
            profile.save() 
        return profile