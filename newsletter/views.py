from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterSignupForm

def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully signed up for the newsletter!')
            return redirect('about')  
    else:
        form = NewsletterSignupForm()
    return render(request, 'newsletter/newsletter_signup.html', {'form': form})

def connect_view(request):
    return render(request, 'newsletter/connect.html')

 