from django.shortcuts import render, get_object_or_404, redirect
from category.models import Category

# Create your views here.

def category_list(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check start

    categories = Category.objects.all()

    return render(request, 'back/category_list.html', {'categories': categories})


def category_add(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check start

    if request.method == 'POST':
        name = request.POST.get('name')

        if name == "":
            error = "All fields are required"
            return render(request, 'back/error.html', {'error': error})
        
        if len(Category.objects.filter(name=name)) != 0:
            error = "Category already exists"
            return render(request, 'back/error.html', {'error': error})
        
        
        b = Category(name=name)
        b.save()
        return redirect('category_list')
    
    return render(request, 'back/category_add.html')