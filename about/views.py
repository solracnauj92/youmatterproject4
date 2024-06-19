from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


# Create your views here.
def about_me(request):
    about = About.objects.all().order_by("-updated_on").first()
    collaborate_form = CollaborateForm()
    
    if request.method == "POST":
        # Process any POST request data here if needed
        messages.add_message(request, messages.SUCCESS, "Message received!")
    
    return render(request, "about/about.html", {
        "about": about,
        "collaborate_form": collaborate_form
    })