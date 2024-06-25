from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import About, CollaborateRequest
from .forms import CollaborateForm
from main_page.models import Post


def about_me(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=request.user.username)
        username = user.username if user.username else ""
        email = user.email if user.email else ""
        collaborate_form = CollaborateForm(
            request.POST or None, initial={'name': username, 'email': email}
        )
    else:
        collaborate_form = CollaborateForm(request.POST or None)
    if request.method == "POST":
        if collaborate_form.is_valid():
            collaborate_form.instance.name = request.user.username
            collaborate_form.save()
            messages.success(
                request,
                "Collaboration request received! I endeavour to respond within 2 working days.")  # noqa
            return redirect('about')
    
    about = About.objects.all().order_by("-updated_on").first()
    
    return render(request, "about/about.html", {
        "about": about,
        "collaborate_form": collaborate_form
    })


def collaboration_requests(request):
    if not request.user.is_superuser:
        messages.error(request, "Access denied - invalid credentials")
        return redirect('about')

    collaborations = CollaborateRequest.objects.filter(approved=False)
    template = "about/collaboration_requests.html"
    context = {
        "collaborations": collaborations,
    }

    return render(request, template, context)


def approve_collaboration_request(request, id):
    if not request.user.is_superuser:
        messages.error(request, "Access denied - invalid credentials")
        return redirect('about')

    # Find the request and approve it
    collaboration = get_object_or_404(CollaborateRequest, id=id)
    collaboration.approved = True
    collaboration.save()

    # Generate a unique title for the Post
    title = f"Collaboration Request {id} - {collaboration.tag}"  # Example of a unique title

    # Check if a Post with the same title already exists
    while Post.objects.filter(title=title).exists():
        title += " (Duplicate)"  # Append to make title unique if needed

    # Create a new instance of the Post model using the requested collab data
    Post.objects.create(
        title=title,
        slug=f"pending-title-{id}",
        author=get_object_or_404(User, username=collaboration.name),
        content=collaboration.message,
        status=1,
        tag=collaboration.tag,
    )
    messages.success(request, 'Collaboration successfully approved')
    return redirect('collaboration_requests')