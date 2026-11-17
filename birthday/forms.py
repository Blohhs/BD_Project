from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from .models import Birthday

BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = ('first_name', 'last_name', 'birthday')
        widgets = {'birthday': forms.DateInput(attrs={'type': 'date'})}

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]

    def clean(self):
        super().clean()
        
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        
        if f'{first_name} {last_name}' in BEATLES:
            send_mail(
                subject='Another Beatles member',
                message=f'{first_name} {last_name} пытался опубликовать запись',
                from_email='s.lapki@gmail.com',
                recipient_list=['s.lapki@gmail.com'],
                fail_silently=False,
            )
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )