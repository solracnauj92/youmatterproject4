from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterSignupForm


def connect_view(request):
    form = NewsletterSignupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'You have successfully signed up for the newsletter!')
            return redirect('connect')  
    
    return render(request, 'newsletter/connect.html', {'form': form}) 

 