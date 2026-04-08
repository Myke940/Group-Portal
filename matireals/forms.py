from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ["title", "description", "file", "image", "url"]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
            "file": forms.FileInput(attrs={'class': 'form-control'}),
            "image": forms.FileInput(attrs={'class': 'form-control'}),
            "url": forms.URLInput(attrs={'class': 'form-control'})
        }