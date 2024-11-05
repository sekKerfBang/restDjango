from django.shortcuts import render
from .models import Product
#from django.http import JsonResponse
#from django.forms.models import model_to_dict
#from rest_framework.response import Response
from .serializers import ProductSerializers
from rest_framework import generics, mixins
from api.mixins import StaffEditorPermissionsMixins

#from .authentications import TokenAuthentication

#  Les classes CBV de django sont geniale et facilite nos differents taches mais cette methode cree beaucoup de class 
# mais on pouvait implementer toute ces fonctionnalites dans  une classe heritant de mixins et des autres classes

# class DetailProductView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers

# class ListProductView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers
    
#     def get_queryset(self):
#         return super().get_queryset().filter(name__icontains='Bonbon')

    
# class CreateProductView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers
    
#     def perform_create(self, serializer):
#         name = serializer.validated_data.get('name')
#         content = serializer.validated_data.get('content') or None
#         if content is None:
#             content = name        
#         serializer.save(content=content)
    
# class UpdateProductView(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers
    
#     def perform_update(self, serializer):
#         name = serializer.validated_data.get('name')
#         content = serializer.validated_data.get('content') or None
#         if content is None:
#             content = name        
#         serializer.save(content=content)
    
# class DeleteProductView(generics.DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers
#     lookup_field = "pk"

class ProductMixinsViews(
    StaffEditorPermissionsMixins,
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"
    # remplacer par un parametre par default de rest_framework #authentication_classes = [authentication.TokenAuthentication, TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser, IsStaffPermission]
    
    def perform_create(self, serializer):
        email = serializer.validated_data.pop('email')
        print(email)
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name        
        serializer.save(content=content)
        
    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name        
        serializer.save(content=content)    
        
    
    
    def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
            return self.partial_update(request, *args, **kwargs)
        
    def get_queryset(self):
        return super().get_queryset().filter(name__icontains='')
    