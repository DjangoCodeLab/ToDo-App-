from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
# Create your views here.

from .forms import *
from .models import Todo
def index(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('todo')
        
        else:
            form = TodoForm()
    page = {
        'forms':form,
    }
    return render(request, 'todo/index.html', page)

def read_data(request):
    item_list = Todo.objects.order_by("-date")

    context = {
        'item_list':item_list
    }

    return render (request, 'todo/info.html',context)


def delete_data(request, id):
    item_list = Todo.objects.filter(id = id)
    item_list.delete()
    print(item_list)
    
   
    return redirect('data')


def update_data(request, id):
    item_list = get_object_or_404(Todo, id = id)
    if request.method == 'POST':
        form = UpdateFrom(request.POST, instance = item_list)

        if form.is_valid():
            form.save()
            return redirect('/', id = item_list.id)
    else:
        form = UpdateFrom(instance = item_list)

    context = {
        'form': form
    }
    return render(request,'todo/update.html',context)
