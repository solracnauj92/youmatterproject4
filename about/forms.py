from .models import CollaborateRequest, Newsletter
from django import forms


class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']