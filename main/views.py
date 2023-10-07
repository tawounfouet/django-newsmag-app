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

from django.contrib.auth.decorators import login_required

#@login_required
def panel(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check start

    return render(request, 'back/panel.html')


from django.contrib.auth import authenticate, login, logout
def mylogin(request):
    
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        if username != '' or password != '':
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('panel')
                
    return render(request, 'front/login.html')


def mylogout(request):

    logout(request)
    
    return redirect("mylogin")