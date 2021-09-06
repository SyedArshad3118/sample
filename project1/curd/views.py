
from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from curd.models import employee
from curd.serializers import curdserializers
from rest_framework.decorators import api_view
import asyncio 
from asgiref.sync import sync_to_async 
from aiohttp import web

@sync_to_async 
@api_view(['GET', 'POST', 'DELETE'])
def curd_list(request):
    if request.method == 'GET':
        emp = employee.objects.all()
        name = request.query_params.get('name', None)
        if name is not None:
            emp = emp.filter(name__icontains=name)
        
        curd_serializer = curdserializers(emp, many=True)
        return JsonResponse(curd_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        curd_data = JSONParser().parse(request)
        curd_serializer = curdserializers(data=curd_data)
        if curd_serializer.is_valid():
            curd_serializer.save()
            return JsonResponse(curd_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(curd_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = employee.objects.all().delete()
        return JsonResponse({'message': '{} curd were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@sync_to_async 
@api_view(['GET','PUT', 'DELETE'])
def curd_detail(request,pk):
    try: 
        emp = employee.objects.get(pk=pk) 
    except employee.DoesNotExist: 
        return JsonResponse({'message': 'The record does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        curd_serializer = curdserializers(emp) 
        return JsonResponse(curd_serializer.data) 
    
    if request.method == 'PUT': 
        curd_data = JSONParser().parse(request) 
        curd_serializer = curdserializers(emp, data=curd_data) 
        if curd_serializer.is_valid(): 
            curd_serializer.save() 
            return JsonResponse(curd_serializer.data) 
        return JsonResponse(curd_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        curd.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
@sync_to_async        
@api_view(['GET'])
def curd(request,name):
    emp = employee.objects.filter(name=name)
    if request.method == 'GET': 
        curd_serializer = curdserializers(emp, many=True)
        return JsonResponse(curd_serializer.data, safe=False)

async def sample(request):
    loop = asyncio.get_event_loop()
    loop.create_task(curd_list())
    loop.create_task(curd_detail())
    return HttpResponse("hai")
 