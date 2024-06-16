from .views import Index, post_detail
from django.urls import path

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('<slug:slug>/', post_detail, name='post_detail'),

]