from django.shortcuts import render
from django.http import JsonResponse

def api_view(request, *args, **kwargs):
    data = {
        'name' : 'Sekhou',
        'language' : 'Python'
    }
    return JsonResponse(data)

