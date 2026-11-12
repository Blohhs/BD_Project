from django.db import models
from django.urls import reverse
from .validators import real_age

class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField('Фамилия', max_length=20, help_text='Необязательное поле', blank=True)
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('birthday:detail', kwargs={'pk': self.pk}) 