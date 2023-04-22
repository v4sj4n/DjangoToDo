from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.
def home(request):
    context = {"todos": Todo.objects.all()}
    return render(request, "base/home.html", context)

def todo(request, pk):
    todo = Todo.objects.get(id=pk)
    context = {"todo": todo}
    return render(request, "base/todo.html", context)


def createTodo(request):
    form = TodoForm
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/todo_form.html", context)

def updateTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/todo_form.html', context)

def deleteTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': todo})
