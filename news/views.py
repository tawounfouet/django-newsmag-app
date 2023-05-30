from django.shortcuts import render, get_object_or_404, redirect
from news.models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from subcategory.models import SubCategory

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

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    
    if len(str(day)) == 1 :
        day = "0" + str(day)
    if len(str(month)) == 1 :
        month = "0" + str(month)

    today = str(year) + "/" + str(month) + "/" + str(day)
    time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)


    categories = SubCategory.objects.all()

    if request.method == 'POST':

        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstextshort = request.POST.get('newstextshort')
        newstext = request.POST.get('newstext')
        newsid = request.POST.get('newscat')
    

        if newstitle == "" or newstextshort == "" or newstext == "" or newscat == "":
            error = "Please fill all fields"
            return render(request, 'back/error.html', {'error': error, 'site': site})
        
        # else:
        #     myfile = request.FILES['myfile']
        #     fs = FileSystemStorage()
        #     filename = fs.save(myfile.name, myfile)
        #     uploaded_file_url = fs.url(filename)

        #     newsname = SubCategory.objects.get(pk=newsid).name 

        #     b = News(title=newstitle, short_description=newstextshort, body=newstext, category=newsname, category_id=newsid,
        #                     author='admin', date=today, time=time, show=0, image=filename, image_url=uploaded_file_url)
        #     b.save()
        #     return redirect('news_list')

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)   

            if str(myfile.content_type).startswith('image'):

                if myfile.size < 5000000:

                    newsname = SubCategory.objects.get(pk=newsid).name

                    b = News(title=newstitle, short_description=newstextshort, body=newstext, category=newsname, category_id=newsid,
                            author='admin', date=today, time=time, show=0, image=filename, image_url=uploaded_file_url)
                    b.save()
                    return redirect('news_list')
                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    
                    error = "Your Image is bigger than 5MB, please upload smaller image"
                    return render(request, 'back/error.html', {'error': error, 'site': site})
            else:
                fs = FileSystemStorage()
                fs.delete(filename)

                error = "Your File Not Supported"
                return render(request, 'back/error.html', {'error': error, 'site': site})
        except:
            error = "Please input your image"
            return render(request, 'back/error.html', {'error': error, 'site': site})
         

   

    return render(request, 'back/news_add.html', {'site': site, 'categories': categories})


def news_delete(request, pk):
    site = Main.objects.get(pk=1)
    #news = get_object_or_404(News, pk=pk)
    #news.delete()
    #b = News.objects.filter(pk=pk)

    try:
        b = News.objects.get(pk=pk)

        # fs = FileSystemStorage()
        # fs.delete(b.image)

        b.delete()
    except:
        error = "Something went wrong"
        return render(request, 'back/error.html', {'error': error, 'site': site})

    return redirect('news_list')