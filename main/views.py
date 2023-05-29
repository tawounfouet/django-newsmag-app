from django.shortcuts import render, get_object_or_404, redirect
from main.models import Main
from news.models import News

# Create your views here.


def home(request):
    # sitename = 'News Mag | Home'
    # site = Main.objects.filter(pk=1)
    site = Main.objects.get(pk=1)
    # sitename = site.title + ' | Home'
    news = News.objects.all()

    return render(request, 'front/home.html', {'site': site, 'news': news})


def about(request):
    # sitename = site.title + ' | About'
    site = Main.objects.get(pk=1)

    return render(request, 'front/about.html', {'site': site})
