from django.urls import path
from .views import *
app_name = 'blog'
urlpatterns = [
path('', ArticleListView.as_view(), name='article-list'),
path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
path('create/', CreateArticleView.as_view(), name='article-create'),
path('<int:id>/update/', UpdateArticleView.as_view(), name='article-update'),
path('<int:id>/delete/', DeleteArticleView.as_view(), name='article-delete'),


]