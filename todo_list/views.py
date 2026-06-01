from django.shortcuts import render, redirect
from django.tasks import task
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
<<<<<<< Updated upstream
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
=======
	if request.method == 'POST':
		form = ListForm(request.POST or None)
		
		if form.is_valid():
			form.save()
			tasks = List.objects.all
			messages.success(request, ("Task Has Been Added To List!"))
			return render(request, 'home.html', {'tasks': tasks}) 

	else:
		tasks = List.objects.all
		return render(request, 'home.html', {'tasks': tasks}) 
>>>>>>> Stashed changes


def about(request):
	context = {'first_name': 'Alireza', 'last_name': 'Ghorbani'}
	return render(request, 'about.html', context)


def delete(request, list_id):
	task = List.objects.get(pk=list_id)
	task.delete()
	messages.success(request, ("Task Has Been Deleted!"))
	return redirect('home')


def cross_off(request, list_id):
<<<<<<< Updated upstream
    task = List.objects.get(pk=list_id)
    task.completed = True
    task.save()
    return redirect('home')


def uncross(request, list_id):
    task = List.objects.get(pk=list_id)
    task.completed = False
    task.save()
    return redirect('home')
=======
	task = List.objects.get(pk=list_id)
	task.completed = True
	task.save()
	return redirect('home')

def uncross(request, list_id):
	task = List.objects.get(pk=list_id)
	task.completed = False
	task.save()
	return redirect('home')
>>>>>>> Stashed changes


def edit(request, list_id):
    task = List.objects.get(pk=list_id)

<<<<<<< Updated upstream
    if request.method == 'POST':
        form = ListForm(request.POST, request.FILES, instance=task)  # Fixed: pass FILES separately
        
        if form.is_valid():
            form.save()
            messages.success(request, ('Task Has Been Edited!'))
            return redirect('home')
    else:
        form = ListForm(instance=task)

    return render(request, 'edit.html', {'task': task, 'form': form})
=======
		form = ListForm(request.POST or None, instance=task)
		
		if form.is_valid():
			form.save()
			messages.success(request, ('Task Has Been Edited!'))
			return redirect('home')

	else:
		task = List.objects.get(pk=list_id)
		return render(request, 'edit.html', {'task': task})
	
	


# password12345
>>>>>>> Stashed changes
