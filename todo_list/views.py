from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST, request.FILES) 
        if form.is_valid():
            task_instance = form.save(commit=False)
            task_instance.time_taken = form.cleaned_data.get('time_taken')
            task_instance.save()
            messages.success(request, ("Task Has Been Added To List!"))
            return redirect('home')  
    else:
        form = ListForm() 

    tasks = List.objects.all()
    return render(request, 'home.html', {'tasks': tasks, 'form': form})


def about(request):
    context = {'first_name': 'Alireza', 'last_name': 'Ghorbani'}
    return render(request, 'about.html', context)


def delete(request, list_id):
    task = List.objects.get(pk=list_id)
    task.delete()
    messages.success(request, ("Task Has Been Deleted!"))
    return redirect('home')


def cross_off(request, list_id):
    task = List.objects.get(pk=list_id)
    task.completed = True
    task.save()
    return redirect('home')

def uncross(request, list_id):
    task = List.objects.get(pk=list_id)
    task.completed = False
    task.save()
    return redirect('home')

def edit(request, list_id):
    task = List.objects.get(pk=list_id)
    
    if request.method == 'POST':
        form = ListForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            task_instance = form.save(commit=False)
            task_instance.time_taken = form.cleaned_data.get('time_taken')
            task_instance.save()
            messages.success(request, ('Task Has Been Edited!'))
            return redirect('home')
    else:
        form = ListForm(instance=task)
        
    return render(request, 'edit.html', {'task': task, 'form': form})