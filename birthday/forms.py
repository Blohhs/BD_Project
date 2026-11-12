from django import forms
from .models import Birthday


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = ('first_name', 'last_name', 'birthday')
        widgets = {'birthday': forms.DateInput(attrs={'type': 'date'})}

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]