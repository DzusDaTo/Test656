from django.db import models
from django.contrib.auth.models import User


class Cat(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    breed = models.CharField(max_length=100, verbose_name='Порода')
    fur_length = models.CharField(max_length=50, verbose_name='Длина шерсти')
    user = models.ForeignKey(User, related_name='cats', on_delete=models.CASCADE, verbose_name='Владелец')

    def __str__(self):
        return self.name

