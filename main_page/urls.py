from .views import Index, post_detail
from django.urls import path, include
from . import views


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
    views.comment_delete, name='comment_delete'),
    path('about/', include('about.urls')),
    
]