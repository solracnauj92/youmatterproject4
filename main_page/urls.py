from .views import Index, post_detail
from django.urls import path
from . import views

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),

]