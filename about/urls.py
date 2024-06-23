from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_page, name='about'),
    path(
        'collaboration_requests/',
        views.collaboration_requests,
        name='collaboration_requests'
    ),
    path(
        'approve_collaboration_request/<int:id>/',
        views.approve_collaboration_request,
        name='approve_collaboration_request'
    ),
]