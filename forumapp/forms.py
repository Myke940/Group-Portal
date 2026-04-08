from django import forms

class MessageForm(forms.Form):
    username = forms.CharField(max_length=50)
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}), max_length=500)




    