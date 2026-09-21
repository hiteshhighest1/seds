from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def index_view(request):
    return render(request, 'core/index.html')

def gallery_view(request):
    return render(request, 'core/gallery.html')

def magazine_view(request):
    return render(request, 'core/magazine.html')

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not email or not message:
            messages.error(request, "Please fill in all required fields.")
            return render(request, "core/contact.html")

        email_subject = subject or f"New message from {name}"

        email_body = f"""
New message received through the SEDS Loyola website.

Name: {name}
Email: {email}
Subject: {subject or "No subject"}

Message:
{message}
"""

        try:
            send_mail(
                subject=email_subject,
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["seds.loyola@sxc.edu.np"],
                reply_to=[email],
                fail_silently=False,
            )

            messages.success(
                request,
                "Your message has been sent successfully!"
            )

        except Exception as e:
            print("Email error:", e)
            messages.error(
                request,
                "There was a problem sending your message."

            )

    return render(request, "core/contact.html")