from django.conf.urls.static import static
from my_project import settings
from .views import *
from django.urls import path


urlpatterns = [
    path('', InfoCats.as_view(), name="info_cats"),
    path('add-article/', AddArticles.as_view(), name='add_article'),
    path('<int:cat_id>/', CatArticle.as_view(), name="cats_article"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

