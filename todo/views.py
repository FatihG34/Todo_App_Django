from django.shortcuts import render,redirect
from django.http import HttpResponse
from todo.forms import TodoForm
from todo.models import Todo
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required




def home(request):
    todos = Todo.objects.all()
    form = TodoForm()
    context = {
        'todos':todos,
        'form': form
    }
    return render(request,'todo/home.html', context)

def todo_create(request):
    form = TodoForm()
    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Todo created successfully")
            return redirect('home')
    context ={
        'form': form
    }
    return render(request, 'todo/todo_add.html', context)


def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")
    context={
        'todo':todo,
        'form':form
    }
    return render(request, 'todo/todo_update.html', context)


def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        messages.warning(request, "Todo deleted!")
        return redirect('home')
    context = {
        'todo':todo
    }
    return render(request, 'todo/todo_delete.html', context)



@login_required
def special(request):
    return render(request, "user_example/special.html")

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']  # same == # form.cleaned_data.get('username') 
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')