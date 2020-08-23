from django.shortcuts import render
from .models import Banner, MyEducation, MyExperience, ContactMe, Skill, Language, Research, Activity
from .forms import ContactForm
from django.contrib import messages


# Create your views here.


def home(request):
    banner = Banner.objects.first()
    activities = Activity.objects.order_by('id')
    skills = Skill.objects.all()
    experiences = MyExperience.objects.order_by('id')
    educations = MyEducation.objects.order_by('id')
    languages = Language.objects.order_by('id')
    researches = Research.objects.order_by('id')
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            ContactMe.objects.create(name=cd['name'], email=cd['email'], subject=cd['subject'], message=cd['message'])
            messages.success(request, ' Your message successfully sent! <i class="fa fa-heart" aria-hidden="true"></i>')
    form = ContactForm()
    context = {
        'banner': banner,
        'activities': activities,
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
        'languages': languages,
        'researches': researches,
        'form': form
    }
    return render(request, 'home/home.html', context)
