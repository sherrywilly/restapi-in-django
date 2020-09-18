from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers
from .models import Task


@api_view(['GET'])
def index_view(request):
    api_urls = {
        'id':'1',
        'name':'sherry wilson',
        'phone':'6238639239',
        'email':'sherrywilson@gmail.com'

    }
    return Response(api_urls)


@api_view(['GET'])
def Tasklist(request):
    tasks = Task.objects.all()
    serializer =TaskSerializers(tasks,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def TaskView(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer =TaskSerializers(tasks,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Taskcreate(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




@api_view(['POST'])
def Taskupdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 



@api_view(['DELETE'])
def Taskdelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('item successfully deleted')