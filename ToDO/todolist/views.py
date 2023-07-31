from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import ToDo

# Create your views here.

def index(request):
    todos = ToDo.objects.all()
    return render(request, 'ToDo/index.html', {'todo_list': todos, 'title': 'The main page'})

@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title:
            todo = ToDo.objects.create(title=title, description=description, is_complete=False)
            todo.save()
            return redirect('index')
    return render(request, 'ToDo/index.html', {'todo_list': ToDo.objects.all()})

def description_page(request, todo_id):
    todo = get_object_or_404(ToDo, id=todo_id)

    return render(request, 'ToDo/description.html', {'todo': todo})

def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')