from .models import Comment, Post, Profile
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'featured_image', 'content', 'status', 'excerpt', 'tag']

class ProfileForm(forms.ModelForm):
    bio = forms.CharField(label='Bio', widget=forms.Textarea(attrs={'rows': 4}))

    class Meta:
        model = Profile
        fields = ['picture', 'bio']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['picture'].widget.attrs.update({'class': 'form-control-file'})

    def save(self, commit=True):
        profile = super(ProfileForm, self).save(commit=False)
        user = User.objects.get(profile=profile)
        user.bio = self.cleaned_data['bio']
        if commit:
            profile.save()
            user.save()
        return profile