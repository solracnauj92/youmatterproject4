from django.urls import path
from . import views

urlpatterns = [
    path('connect/', views.connect_view, name='connect'),
]
