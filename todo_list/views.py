from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.db.models import Q
from django.utils.dateparse import parse_date

def home(request):

    # -------------------
    # POST (Add Task)
    # -------------------
    if request.method == 'POST':
        form = ListForm(request.POST, request.FILES)

        if form.is_valid():
            task_instance = form.save(commit=False)
            task_instance.time_taken = form.cleaned_data.get('time_taken')
            task_instance.save()

            messages.success(request, "Task Has Been Added To List!")
            return redirect('home')

    # -------------------
    # GET (Filters/Search)
    # -------------------
    form = ListForm()
    tasks = List.objects.all()

    # SEARCH
    search = request.GET.get('search')
    if search:
        tasks = tasks.filter(
            Q(item__icontains=search) |
            Q(side_note__icontains=search)
        )

    # STATUS FILTER
    status = request.GET.get('status')
    if status == "completed":
        tasks = tasks.filter(completed=True)
    elif status == "pending":
        tasks = tasks.filter(completed=False)

    # PRIORITY FILTER
    priority = request.GET.get('priority')
    if priority:
        tasks = tasks.filter(priority=priority)

    # DATE RANGE FILTER (optional fields)
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date:
        tasks = tasks.filter(due_date__date__gte=parse_date(start_date))

    if end_date:
        tasks = tasks.filter(due_date__date__lte=parse_date(end_date))

    # SORTING
    sort = request.GET.get('sort')

    if sort == "due_asc":
        tasks = tasks.order_by('due_date')
    elif sort == "due_desc":
        tasks = tasks.order_by('-due_date')
    elif sort == "name_asc":
        tasks = tasks.order_by('item')
    elif sort == "name_desc":
        tasks = tasks.order_by('-item')
    elif sort == "priority_high":
        tasks = tasks.order_by('-priority')
    elif sort == "priority_low":
        tasks = tasks.order_by('priority')
    elif sort == "time_asc":
        tasks = tasks.order_by('time_taken')
    elif sort == "time_desc":
        tasks = tasks.order_by('-time_taken')

    return render(request, 'home.html', {
        'tasks': tasks,
        'form': form
    })

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