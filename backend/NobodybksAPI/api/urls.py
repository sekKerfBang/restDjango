from django.urls import path
from .views import api_view

urlpatterns = [
    path('', api_view, name='api_view'),
]
#endpoint = 'http://127.0.0.1:8081/api'
