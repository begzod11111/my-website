# Generated by Django 4.2.1 on 2023-06-23 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_cats', '0008_alter_articlecat_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользовател', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='password_2',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_user',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='default/user/404.jpeg', upload_to='cats/info_cats'),
        ),
    ]
