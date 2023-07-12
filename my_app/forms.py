from django.forms import *
from .models import *


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('name', 'last_name', 'email_user', 'photo', 'password', 'password_2')
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'

            }),
            'email_user': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your email'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'your password'
            }),
            'password_2': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'repeat your password'
            })
        }
        labels = {
            'name': '',
            "last_name": "",
            "email_user": "",
            "password_2": "",
            'password': "",
            "photo": "",
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        for i in punctuation:
            if i in name:
                raise ValidationError("error")
        return name

    def clean(self):
        clean_data = super().clean()
        password = clean_data.get("password")
        password_2 = clean_data.get("password_2")
        if password != password_2:
            raise ValidationError("jhjfh")
        return clean_data





