from .views import Index, post_detail, PostUpdateView, PostDeleteView, PostUpdateUserView, toggle_like
from django.urls import path, include
from . import views


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('guidelines/', views.guidelines, name='guidelines'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/update-user/<slug:slug>/', PostUpdateUserView.as_view(), name='post_update_user'),
    path('<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
    views.comment_delete, name='comment_delete'),
    path('about/', include('about.urls')),
    path('post/<int:post_id>/toggle_like/', views.toggle_like, name='toggle_like'),
    path('login/', views.login_view, name='login'),

    

]