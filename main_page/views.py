from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.generic import ListView


# Create your views here.
class Index(ListView):
    model = Post
    template_name = 'main_page/index.html'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(status=1)