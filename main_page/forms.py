from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'featured_image', 'content', 'status', 'excerpt', 'tag']

class PostUpdateUserForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'featured_image', 'content', 'tag']  # Only include the fields that users can modify

    def clean_featured_image(self):
        featured_image = self.cleaned_data.get('featured_image')
        if featured_image:
            # Check if the file size exceeds 10 MB (10 * 1024 * 1024 bytes)
            max_size = 10 * 1024 * 1024
            if featured_image.size > max_size:
                raise forms.ValidationError('File size too large. Maximum is 10 MB.')
        return featured_image