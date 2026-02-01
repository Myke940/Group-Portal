from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile

class RegisterViewForm(UserCreationForm):
    bio = forms.CharField(required = False, label = 'Bio', widget = forms.Textarea())
    profile_picture = forms.ImageField(required = False, label = 'Avatar')
    class Meta():
        model = User
        fields = ['username','password1','password2','bio','profile_picture']
    def save(self):
        user = super().save()
        if not Userprofile.objects.filter(user = user).exists():
            Userprofile.objects.create(user = user, bio = self.cleaned_data['bio'], profile_picture = self.cleaned_data['profile_picture'])
        else:
            profile = user.userprofile
            profile.bio = self.cleaned_data['bio']
            if self.cleaned_data['profile_picture']:
                profile.profilepicture = self.cleaned_data['profile_picture']

        return user
                