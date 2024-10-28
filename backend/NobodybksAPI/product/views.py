from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
#from rest_framework.decorators import api_view
from .serializers import ProductSerializers
from rest_framework import generics

class DetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    

