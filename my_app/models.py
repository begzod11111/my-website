from string import punctuation

from django.core.exceptions import ValidationError
from django.db.models import *
# Create your models here.


class User(Model):
    name = CharField(max_length=20)
    last_name = CharField(max_length=20, blank=True)
    email_user = EmailField(max_length=200)
    photo = ImageField(upload_to="cats/info_cats", blank=True, default='default/user/404.jpeg')
    password = CharField(max_length=16)
    password_2 = CharField(max_length=16)

    def __str__(self):
        return f"{self.name} - {self.last_name}"

    class Meta:
        verbose_name = 'Пользовател'
        verbose_name_plural = 'Пользователи'





