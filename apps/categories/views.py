from django.shortcuts import render, get_object_or_404
from .models import Category
from .forms import CategoryForm


# Create your views here.
def category_list(required):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories':categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'categories/category_detail.html', {'category':category})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    else:
        form = CategoryForm()

    return render(request, 'categories/category_create.html', {'form': form})
