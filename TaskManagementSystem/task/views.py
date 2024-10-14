from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskModelForm
from .import views
def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'task/show_tasks.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            form.save_m2m()
            return redirect('show_tasks') 
    else:
        form = TaskModelForm()  
    return render(request, 'task/add_task.html', {'form': form})

def edit_task(request, pk):
    task = TaskModel.objects.filter(pk=pk).first()  
    if task is None:
        return render(request, 'task/error.html', {'message': 'Task not found.'})

    if request.method == 'POST':
        form = TaskModelForm(request.POST, instance=task)  
        if form.is_valid():
            form.save()
            return redirect('show_tasks') 
    else:
        form = TaskModelForm(instance=task)
    return render(request, 'task/edit_task.html', {'form': form})


def delete_task(request, pk):
    task = TaskModel.objects.filter(pk=pk).first()
    
    if task is not None:
        task.delete()
        return redirect('show_tasks')
    else:
        return render(request, 'task/error.html', {'message': 'Task not found.'})


def complete_task(request, task_id):
    task = TaskModel.objects.filter(pk=task_id).first()  
    if task is not None:
        task.is_completed = True
        task.save()
        return redirect('show_tasks')  
    else:
        return render(request, 'task/error.html', {'message': 'Task not found.'})
