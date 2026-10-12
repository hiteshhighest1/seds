from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse

def sitemap_xml(request):
    base_url = "https://sedsloyola.vercel.app"

    paths = [
        "/",
        "/gallery.html",
        "/contact.html",
        "/magazine.html",
    ]

    urls = "".join(
        f"<url><loc>{base_url}{path}</loc></url>"
        for path in paths
    )

    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f'{urls}'
        '</urlset>'
    )

    return HttpResponse(xml, content_type="application/xml")

def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Allow: /\n\n"
        "Sitemap: https://sedsloyola.vercel.app/sitemap.xml\n"
    )

    return HttpResponse(content, content_type="text/plain")

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
            email_message = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=["seds.loyola@sxc.edu.np"],
                reply_to=[email],
            )

            email_message.send(fail_silently=False)

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