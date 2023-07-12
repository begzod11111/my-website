# Generated by Django 4.2.1 on 2023-06-23 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info_cats', '0006_alter_articlecat_options_alter_articlecat_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('email_user', models.EmailField(blank=True, max_length=254, null=True)),
                ('photo', models.ImageField(null=True, upload_to='cats/info_cats')),
            ],
        ),
        migrations.AlterField(
            model_name='articlecat',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='info_cats.user'),
        ),
        migrations.DeleteModel(
            name='Cat',
        ),
    ]
