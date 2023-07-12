from django.shortcuts import render, redirect
from django.views.generic import *

from .models import ArticleCat
from .forms import *
# Create your views here.


class InfoCats(ListView):
    model = ArticleCat
    template_name = 'info_cats/info.html'
    context_object_name = 'content'


class CatArticle(DetailView):
    model = ArticleCat
    template_name = "info_cats/cats_article.html"
    pk_url_kwarg = 'cat_id'
    context_object_name = 'a'


class AddArticles(CreateView):
    form_class = ArticleForm
    template_name = 'info_cats/add_article.html'


# def add_art(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # return redirect('info_cats')
#     else:
#         form = ArticleForm()
#     return render(request, 'info_cats/add_article.html', context={"form": form})




