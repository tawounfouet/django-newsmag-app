from django.shortcuts import render, get_object_or_404, redirect
from news.models import News
from main.models import Main

# Create your views here.

def news_detail(request, pk):
    #news = News.objects.all
    news = News.objects.filter(pk=pk)
    site = Main.objects.get(pk=1)
    #news = get_object_or_404(News, pk=pk)
    return render(request, 'front/news_detail.html', {'news': news, 'site': site})


def news_list(request):
    news = News.objects.all()
    site = Main.objects.get(pk=1)
    return render(request, 'back/news_list.html', {'news': news, 'site': site})


