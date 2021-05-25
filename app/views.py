from django.shortcuts import render
from .models import Todo
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TodoSerializer

# Create your views here.


@api_view(['GET'])
def todo_view (request):

    todo=Todo.objects.all()
    serializer = TodoSerializer(todo,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def todo_task(request,id):

    task=Todo.objects.get(id=id)
    
    serializer = TodoSerializer(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def update_task(request,id):
    task=Todo.objects.get(id=id)
    serializer=TodoSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    


@api_view(['DELETE'])
def delete_task(request,id):
    task=Todo.objects.get(id=id)
    task.delete()
    task2=Todo.objects.all()
    serializer= TodoSerializer(task2,many=True)
    return Response(serializer.data)