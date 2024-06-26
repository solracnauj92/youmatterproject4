from django.contrib import admin
from .models import Post, Comment, Tag
from django_summernote.admin import SummernoteModelAdmin
from .forms import PostUpdateUserForm, PostForm

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # Default form for regular users
    form = PostUpdateUserForm

    list_display = ('title', 'slug', 'status', 'tag')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            # Superuser gets a different form
            kwargs['form'] = PostForm
        else:
            # Regular users get the default form
            kwargs['form'] = self.form
        return super().get_form(request, obj, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []  # Superusers can edit everything
        return ['author', 'status']

# Register your models here.
admin.site.register(Comment)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)





