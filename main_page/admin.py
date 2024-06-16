from django.contrib import admin
from .models import Post, Comment, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')
    search_fields = ('name',)