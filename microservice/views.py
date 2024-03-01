from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
from django.http import JsonResponse
import json
@csrf_exempt
def send_random_JSON(request):
    print('send_random_JSON')
    if request.method == 'GET':
        return JsonResponse({'message': 'Hello from django'})
    else:
        return JsonResponse({'message': 'Unsupported HTTP method'})