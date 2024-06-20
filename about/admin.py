from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin
from .models import CollaborateRequest

# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
# Register your models here.

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)

