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


def news_add(request):
    site = Main.objects.get(pk=1)

    if request.method == 'POST':

        newstitle = request.POST.get('newstitle')
        #newscat = request.POST.get('newscat')
        newstextshort = request.POST.get('newstextshort')
        newstext = request.POST.get('newstext')
    

        if newstitle == "" or newstextshort == "" or newstext == "":
            error = "Please fill all fields"
            return render(request, 'back/error.html', {'error': error, 'site': site})
        
        b = News(title=newstitle, short_description=newstextshort, body=newstext,  category_id=1,
                  author='admin', date='2019-01-01 00:00:00', show=True)
        b.save()
        return redirect('news_list')
 

       
        # title = request.POST['title']
        # content = request.POST['content']
        # author = request.POST['author']
        # image = request.FILES['image']
        # news = News(title=title, content=content, author=author, image=image)
        # news.save()
        return redirect('news_list')

    return render(request, 'back/news_add.html', {'site': site})