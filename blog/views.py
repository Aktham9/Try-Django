from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

# Create your views here.

class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "articles/article_list.html"

class ArticleDetailView(DetailView):
    model = Article
    pk_url_kwarg = "id"
    context_object_name = "article"
    template_name = "articles/article_detail.html"

class CreateArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "articles/article_form.html"
    # success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) ## retrun to get_absolute_url

    # def get_success_url(self):
    #     return "/"
class UpdateArticleView(UpdateView):
    model = Article
    pk_url_kwarg = "id"
    form_class = ArticleForm
    template_name = "articles/article_form.html"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) ## retrun to get_absolute_url

class DeleteArticleView(DeleteView):
    model = Article
    pk_url_kwarg = "id"
    context_object_name = "article"
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy("blog:article-list")








