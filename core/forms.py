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

    def save(self, commit = True):
        user = super().save(commit = False)  #  спочатку зберігаємо юзера без commit
        if commit:
            user.save()                    # тепер точно зберігаємо юзера

            profile, created = Userprofile.objects.get_or_create(user=user)
            profile.bio = self.cleaned_data['bio']
            if self.cleaned_data['profile_picture']:
                profile.profile_picture = self.cleaned_data['profile_picture']
            profile.save()

        return user
                