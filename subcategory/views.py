from django.shortcuts import render, get_object_or_404, redirect
from subcategory.models import SubCategory
from category.models import Category

# Create your views here.

def subcategory_list(request):
    subcategories = SubCategory.objects.all()

    return render(request, 'back/subcategory_list.html', {'subcategories': subcategories})


def subcategory_add(request):

    categories = Category.objects.all()


    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')

        if name == "":
            error = "All fields are required"
            return render(request, 'back/error.html', {'error': error})
        
        if len(SubCategory.objects.filter(name=name)) != 0:
            error = "SubCategory already exists"
            return render(request, 'back/error.html', {'error': error})
        
        category_name = Category.objects.get(pk=category_id).name

        b = SubCategory(name=name, category_name=category_name, category_id=category_id)
        b.save()
        return redirect('subcategory_list')
    
    return render(request, 'back/subcategory_add.html', {'categories': categories})