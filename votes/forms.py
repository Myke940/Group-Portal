from django import forms
from django.forms import inlineformset_factory
from .models import Vote, VoteOption

# Форма для створення нових голосувань
class VoteForm(forms.Form):
    class Meta:
        model = Vote
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

VoteOptionFormSet = inlineformset_factory(
    Vote,                 
    VoteOption,             
    fields=['text'],
    extra=3,               
    can_delete=False,
    widgets={'text': forms.TextInput(attrs={'class': 'form-control'})},
)

class VoteOptionFormSet(VoteOptionFormSet):
    # Перевизначаємо метод, який викликається під час валідації formset для перевірки даних на рівні набору форм
    def clean(self):
        super().clean()
        if self.is_valid():
            # створюємо список форм, у яких поле text заповнене (не порожнє)
            filled_forms = [form for form in self.forms if form.cleaned_data.get('text')]
            if len(filled_forms) < 2:
                raise forms.ValidationError('At least two answer options are required.')