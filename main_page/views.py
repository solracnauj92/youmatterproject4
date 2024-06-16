from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from django.views.generic import ListView


# Create your views here.
class Index(ListView):
    model = Post
    template_name = 'main_page/index.html'
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
        """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(request, 'main_page/post_detail.html', {'post': post})