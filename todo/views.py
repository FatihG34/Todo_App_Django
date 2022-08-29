from django.shortcuts import render
from django.http import HttpResponse
from todo.forms import TodoForm

from todo.models import Todo

def home(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos
    }
    return render(request,'todo/home.html', context)

def todo_create(request):
    form = TodoForm()

    context ={
        'form': form
    }
    return render(request, 'todo/todo_add.html', context)