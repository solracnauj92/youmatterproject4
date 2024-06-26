from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post, Comment
from .forms import CommentForm, PostForm, PostUpdateUserForm
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .utils import resize_image


# Create your views here.
class Index(ListView):
    model = Post
    template_name = 'main_page/index.html'
    paginate_by = 6

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    is_liked = post.is_liked_by(request.user) if request.user.is_authenticated else False

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )

    comment_form = CommentForm()

    return render(
        request,
        'main_page/post_detail.html', 
        {
            'post': post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "is_liked": is_liked,

        }
    )

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'main_page/post_update.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug=self.kwargs['slug'])

@method_decorator(login_required, name='dispatch')
class PostUpdateUserView(UpdateView):
    model = Post
    form_class = PostUpdateUserForm
    template_name = 'main_page/post_update_user.html'
    success_url = reverse_lazy('home')  # Adjust as per your URL setup

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug=self.kwargs['slug'])

    def form_valid(self, form):
        try:
            self.object = form.save(commit=False)
            self.object.save()
            return super().form_valid(form)
        except Exception as e:
            form.add_error(None, str(e))
            return self.form_invalid(form)

@method_decorator(login_required, name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'main_page/post_confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Post, slug=self.kwargs['slug'])

@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.is_liked_by(request.user):
        post.unlike(request.user)
        messages.add_message(request, messages.SUCCESS, 'You unliked the post.')
    else:
        post.like(request.user)
        messages.add_message(request, messages.SUCCESS, 'You liked the post.')
    return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))

def guidelines(request):
    return render(request, 'main_page/guidelines.html')

def upload_image(request):
    if request.method == 'POST':
        form = PostUpdateUserForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            
            # Check if a new image is uploaded
            if instance.featured_image:
                try:
                    # Resize the image
                    resized_image = resize_image(instance.featured_image.path, 256, 256)
                    
                    # Upload the resized image to Cloudinary
                    uploaded_image = cloudinary.uploader.upload(resized_image)
                    
                    # Update the featured_image field with the Cloudinary URL
                    instance.featured_image = uploaded_image['secure_url']
                except Exception as e:
                    print(f"Error resizing and uploading image: {str(e)}")
            
            # Save the instance (whether with updated image or not)
            instance.save()
            
            return redirect('success_page')  # Replace with your success URL name
    else:
        form = PostUpdateUserForm()
    
    return render(request, 'upload_form.html', {'form': form})

def handle_uploaded_file(request):
    try:
        # Process the file upload to Cloudinary here
        # Example: cloudinary.uploader.upload(file)
        pass
    except CloudinaryError as e:
        if 'RequestDataTooBig' in str(e):
            return HttpResponseBadRequest("File size too large. Maximum is 10 MB.")
        else:
            return HttpResponseBadRequest("An error occurred during file upload.")