from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST, request.FILES)  # Fixed: pass FILES separately
        
        if form.is_valid():
            form.save()
            messages.success(request, ("Task Has Been Added To List!"))
            return redirect('home')  # Fixed: redirect to avoid form resubmission

    else:
        form = ListForm()  # Fixed: pass empty form to template

    tasks = List.objects.all()  # Fixed: was missing ()
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
        form = ListForm(request.POST, request.FILES, instance=task)  # Fixed: pass FILES separately
        
        if form.is_valid():
            form.save()
            messages.success(request, ('Task Has Been Edited!'))
            return redirect('home')
    else:
        form = ListForm(instance=task)

    return render(request, 'edit.html', {'task': task, 'form': form})
