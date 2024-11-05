from .models import Product
from .serializers import ProductSerializers
from rest_framework import mixins, viewsets

class ProductViewsets(viewsets.ModelViewSet):
    """  
    get -> list -> QuerySet
    get -> retrieve
    post -> create
    put -> update
    patch -> partial update
    delete -> destroy
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
class ProductListRetrieveDestroyViewset(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers