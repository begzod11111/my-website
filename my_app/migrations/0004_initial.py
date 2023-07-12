# Generated by Django 4.2.1 on 2023-06-25 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_app', '0003_delete_cats_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('email_user', models.EmailField(max_length=200)),
                ('photo', models.ImageField(blank=True, default='default/user/404.jpeg', upload_to='cats/info_cats')),
                ('password', models.CharField(max_length=16)),
                ('password_2', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name': 'Пользовател',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
