from django.shortcuts import render
import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
        # print(data)
    except:
        pass
    print("data: ")
    print(data.keys())
    data['headers']=dict(request.headers)
    data['params'] = dict(request.GET)
    data['content_type'] = request.content_type
    # print(request.GET)
    # print(request.POST)
    print(data)
    return JsonResponse({"message":"Hi there, this is you Django API response!!"})

# Create your views here.
