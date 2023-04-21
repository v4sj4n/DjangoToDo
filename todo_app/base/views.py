from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.
def home(request):
    context = {"todos": Todo.objects.all()}
    return render(request, "base/home.html", context)

def createTodo(request):
    form = TodoForm
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/new_todo.html", context)

def todo(request, pk):
    todo = Todo.objects.get(id=pk)
    context = {"todo": todo}
    return render(request, "base/todo.html", context)