from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_me, name='about'),
    path('newsletter/signup/', views.newsletter_signup, name='newsletter_signup'),
] 