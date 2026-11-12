from django.db import models
# Импортируем наш валидатор
from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', max_length=20, help_text='Необязательное поле', blank=True
    )
    birthday = models.DateField('Дата рождения', validators=(real_age,))