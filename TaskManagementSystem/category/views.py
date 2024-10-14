from django.shortcuts import render,redirect
from .models import TaskCategory
from .forms import TaskCategoryForm

def show_categories(request):
    categories = TaskCategory.objects.all()
    return render(request, 'category/show_category.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = TaskCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_categories')  
    else:
        form = TaskCategoryForm()
    return render(request, 'category/add_category.html', {'form': form})
