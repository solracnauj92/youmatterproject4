from django.shortcuts import render
from django.contrib import messages
from .models import About, Newsletter
from .forms import CollaborateForm, NewsletterForm


# Create your views here.
def about_me(request):

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        newsletter_form = NewsletterForm()
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")
    about = About.objects.all().order_by("-updated_on").first()
    collaborate_form = CollaborateForm()
    
    if request.method == "POST":
        # Process any POST request data here if needed
        messages.add_message(request, messages.SUCCESS, "Message received!")

    if 'newsletter' in request.POST:
            newsletter_form = NewsletterForm(data=request.POST)
            if newsletter_form.is_valid():
                newsletter_form.save()
                messages.add_message(request, messages.SUCCESS, "Thank you for signing up for our newsletter!")
                return redirect('about_me')

    if 'newsletter_form' not in locals():
        newsletter_form = NewsletterForm()
    
    return render(request, "about/about.html", {
        "about": about,
        "collaborate_form": collaborate_form,
        "newsletter_form": newsletter_form
    })