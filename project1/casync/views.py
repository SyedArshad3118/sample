from django.shortcuts import render
from time import sleep                                                 
from django.http import JsonResponse,HttpResponse
import asyncio
import httpx
# Create your views here.
'''
def api(request):
    time.sleep(1)
    payload={"message":"hello  from django!"}
    if "task_id" in request.GET:
        payload["task_id"] = request.GET['task_id']
    return JsonResponse(payload)

'''
async def sample():
    for num in range(1,6):
        await asyncio.sleep(1)
        print(num)
        for i in [10,20,30,40,50]:
            await asyncio.sleep(1)
            print(i) 
        
async def async_view(request):
    task = asyncio.create_task(sample())
    await task
    return HttpResponse('non-blocking http request')



