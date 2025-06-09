
from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all()
    tasks = Task.objects.all().order_by('-created_at') 
    return render(request, 'todo/home.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
    return redirect('todo_home')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('todo_home')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('todo_home')




# Create your views here.
