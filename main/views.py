from django.shortcuts import render, get_object_or_404, redirect
from main.models import Main
from news.models import News
from category.models import Category
from subcategory.models import SubCategory

# Create your views here.


def home(request):
    # sitename = 'News Mag | Home'
    # site = Main.objects.filter(pk=1)
    site = Main.objects.get(pk=1)
    # sitename = site.title + ' | Home'
    news = News.objects.all().order_by('-pk')
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    return render(request, 'front/home.html', {'site':site, 'news':news, 'categories':categories, 'subcategories':subcategories})


def about(request):
    # sitename = site.title + ' | About'
    site = Main.objects.get(pk=1)

    return render(request, 'front/about.html', {'site': site})

def panel(request):
    # sitename = site.title + ' | About'
    site = Main.objects.get(pk=1)

    return render(request, 'back/panel.html', {'site': site})
