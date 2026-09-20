from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Newsletter, TeamMember, ContactMessage

def index_view(request):
    newsletters = Newsletter.objects.all().order_by('-issue_date')[:3]
    return render(request, 'core/index.html', {'newsletters': newsletters})

def gallery_view(request):
    return render(request, 'core/gallery.html')

def team_view(request):
    mentors_advisors = TeamMember.objects.filter(role__in=['Mentor', 'Advisor'])
    executives = TeamMember.objects.filter(role='Executive')
    context = {
        'mentors_advisors': mentors_advisors,
        'executives': executives
    }
    return render(request, 'core/team.html', context)

def magazine_view(request):
    magazine = Newsletter.objects.all().order_by('-issue_date')
    return render(request, 'core/magazine.html', {'magazines': magazine})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        messages.success(request, 'Your message has been sent successfully to the SEDS-Loyola team!')
        return redirect('contact')
        
    return render(request, 'core/contact.html')