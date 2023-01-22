
from django.shortcuts import render
from .models import Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def taskCreate(request):
    return render(request, 'create_task.html')

@api_view(['POST'])
def taskAdd(request):
    task = request.POST['task']
    todo = Todo(task=task, completed=False)
    todo.save()
    return render(request, 'todo_list.html', {'todos': Todo.objects.all()})

@api_view(['GET'])
def get_todo_list(request):
    return render(request, 'todo_list.html', {'todos': Todo.objects.all()})


@api_view(['POST'])
def complete_todo(request):
    todo_id = request.GET['todo_id']
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return render(request, 'todo_list.html', {'todos': Todo.objects.all()})

@api_view(['POST'])
def delete_todo(request):
    todo_id = request.GET['todo_id']
    print('===>' ,todo_id)
    Todo.objects.get(id=todo_id).delete()
    return render(request, 'todo_list.html', {'todos': Todo.objects.all()})

