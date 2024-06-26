from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView
from .models import Comment, Post
from django import forms
from .utils import resize_image, handle_image_upload
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import ValidationError


import cloudinary.uploader
import io
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'featured_image', 'content', 'status', 'excerpt', 'tag']

    def clean_featured_image(self):
        return handle_image_upload(self)

class PostUpdateUserForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'featured_image', 'content', 'tag']

    def clean_featured_image(self):
        return handle_image_upload(self)

def handle_image_upload(form):
    featured_image = form.cleaned_data.get('featured_image')

    if isinstance(featured_image, InMemoryUploadedFile):
        if featured_image.size > 10 * 1024 * 1024:  # 10 MB limit
            raise forms.ValidationError("File size is too large. Please upload a picture less than 10MB.")

        try:
            # Resize the image
            resized_image = resize_image(featured_image, 800, 600)

            # Upload the resized image to Cloudinary
            uploaded_image = cloudinary.uploader.upload(resized_image, folder="uploads")

            # Update the featured_image field with the Cloudinary URL
            form.instance.featured_image = uploaded_image['secure_url']
        except forms.ValidationError as e:
            if 'File size too large' in str(e):
                raise forms.ValidationError("File size is too large. Please upload a picture less than 10MB.")
            else:
                raise forms.ValidationError(f"Error uploading image to Cloudinary: {str(e)}")
        except Exception as e:
            raise forms.ValidationError(f"An unexpected error occurred: {str(e)}")

    return featured_image

    