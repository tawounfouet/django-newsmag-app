from django.shortcuts import render, get_object_or_404, redirect
from news.models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from subcategory.models import SubCategory
from category.models import Category

# Create your views here.

def news_detail(request, pk):
    #news = News.objects.all
    news = News.objects.filter(pk=pk)
    site = Main.objects.get(pk=1)
    #news = get_object_or_404(News, pk=pk)



    return render(request, 'front/news_detail.html', {'news': news, 'site': site})


def news_list(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check start

    news = News.objects.all()
    site = Main.objects.get(pk=1)
    return render(request, 'back/news_list.html', {'news': news, 'site': site})


def news_add(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check start

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
    
        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)   

            if str(myfile.content_type).startswith('image'):

                if myfile.size < 5000000:

                    newsname = SubCategory.objects.get(pk=newsid).name
                    ocategory_id = SubCategory.objects.get(pk=newsid).category_id

                    b = News(title=newstitle, short_description=newstextshort, body=newstext, category=newsname,
                              category_id=newsid, ocategory_id=ocategory_id,
                            author='admin', date=today, time=time, show=0, image=filename, image_url=uploaded_file_url)
                    b.save()

                    count = len(News.objects.filter(ocategory_id=ocategory_id))

                    b = Category.objects.get(pk=ocategory_id)
                    b.count = count
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

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check start

    site = Main.objects.get(pk=1)
    #news = get_object_or_404(News, pk=pk)
    #news.delete()
    #b = News.objects.filter(pk=pk)

    try:
        b = News.objects.get(pk=pk)

        # fs = FileSystemStorage()
        # fs.delete(b.image)

        ocategory_id = News.objects.get(pk=pk).ocategory_id

        b.delete()
        
        count = len(News.objects.filter(ocategory_id=ocategory_id))

        m = Category.objects.get(pk=ocategory_id)
        m.count = count
        m.save()

       
    except:
        error = "Something went wrong"
        return render(request, 'back/error.html', {'error': error, 'site': site})

    return redirect('news_list')



def news_edit(request, pk):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check start

    if len(News.objects.filter(pk=pk)) == 0:
        error = "News Not Found"
        return render(request, 'back/error.html', {'error': error})

    site = Main.objects.get(pk=1)
    news = News.objects.get(pk=pk)
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
    
        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)   

            if str(myfile.content_type).startswith('image'):

                if myfile.size < 5000000:

                    newsname = SubCategory.objects.get(pk=newsid).name

                    b = News.objects.get(pk=pk)
                    
                    # fss = FileSystemStorage()
                    # fss.delete(filename)

                    b.title = newstitle
                    b.short_description = newstextshort
                    b.body = newstext
                    b.category = newsname
                    b.category_id = newsid
                    b.image = filename
                    b.image_url = uploaded_file_url

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
            newsname = SubCategory.objects.get(pk=newsid).name

            b = News.objects.get(pk=pk)
                            
            b.title = newstitle
            b.short_description = newstextshort
            b.body = newstext
            b.category = newsname
            b.category_id = newsid
  
            b.save()

            return redirect('news_list')

    return render(request, 'back/news_edit.html', {'site': site, 'pk': pk, 'news': news, 'categories': categories})