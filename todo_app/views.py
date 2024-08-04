from django.shortcuts import render
from .models import Todo
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    todo_items = Todo.objects.all().order_by("-added_date")

    return render(request, 'main/index.html', {
        "todo_items": todo_items
    })


def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    todo = Todo.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect("/")


def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return HttpResponseRedirect("/")

