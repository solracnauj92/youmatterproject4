from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('guidelines/', views.guidelines, name='guidelines'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/update/', views.PostUpdateView.as_view(), name='post_update'),  # noqa
    path('post/update-user/<slug:slug>/', views.PostUpdateUserView.as_view(), name='post_update_user'),  # noqa
    path('<slug:slug>/delete_confirm/', views.post_confirm_delete, name='post_delete_confirm'),  # noqa
    path('<slug:slug>/delete/', views.post_delete, name='post_delete'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
    views.comment_delete, name='comment_delete'),
    path('about/', include('about.urls')),
    path('post/<int:post_id>/toggle_like/', views.toggle_like, name='toggle_like'),  # noqa
    path('login/', views.login_view, name='login'),

]
