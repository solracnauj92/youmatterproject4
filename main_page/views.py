from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    model = Post
    template_name = 'main_page/post_list.html'  # Specify the template to use

    def get_queryset(self):
        """Return the queryset of posts."""
        return Post.objects.filter(status=1)