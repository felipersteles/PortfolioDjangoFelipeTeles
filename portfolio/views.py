

from unicodedata import category
from django.shortcuts import render
from .models import Home, About, Profile, Category, Skill, Portfolio

# Create your views here.

def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()


    context = {
        'home'          : home,
        'about'         : about,
        'profiles'      : profiles,
        'categories'    : categories,
        'portfoloios'   : portfolios,
    }

    return render(request, 'index.html', context)
