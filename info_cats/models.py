from django.db.models import *
from django.urls import reverse
from my_app.models import User


class ArticleCat(Model):
    title = CharField(max_length=20)
    text = TextField(blank=True)
    publish_date = DateField(auto_now=True)
    font = ImageField(upload_to='article_cat/font/%y/%m/%d', blank=True, default='default/user/404.jpeg')
    author = ForeignKey(User, on_delete=CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.author.name} - {self.title}'

    def get_absolute_url(self):
        return reverse('cats_article', kwargs={'cat_id': self.pk})

    class Meta:
        ordering = ['-publish_date', ]
