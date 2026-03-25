from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactMessageForm   # make sure this import matches your folder structure
from .models import *                   # Profile, About, Skill, Project, Education, Contact


def portfolio(request):
    # Fetch all your data (same as before)
    profile = Profile.objects.first()
    about = About.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    education = Education.objects.all()
    contact = Contact.objects.first()

    # Initialize the form
    form = ContactMessageForm()

    # Handle form submission
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Build the email body
            full_message = (
                f"New message from your portfolio website:\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Subject: {subject}\n\n"
                f"Message:\n{message}\n"
            )

            try:
                send_mail(
                    subject=f"Portfolio message from {name} - {subject}",
                    message=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],  # send to yourself
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully! Thank you.")
                return redirect('portfolio')  # or whatever name your URL has
            except Exception as e:
                # In production, you might want to log the error
                messages.error(request, "Sorry, there was a problem sending your message. Please try again later.")
                # You can also print(e) during development to debug

    # Prepare context for the template
    context = {
        'profile': profile,
        'about': about,
        'skills': skills,
        'projects': projects,
        'education': education,
        'contact': contact,
        'form': form,               # ← this is new – pass the form to the template
    }

    return render(request, 'index.html', context)