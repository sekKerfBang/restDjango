from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse

class ProductSerializers(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    #url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product:detail', lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    class Meta: 
        model = Product 
        fields = ('email', 'url', 'pk', 'name', 'content', 'price', 'my_discount')
        
    # def create(self, validated_data):
    #     print(validated_data)
    #     email = validated_data.pop('email')
    #     print(email)
    #     print(validated_data)
    #     #return Product.objects.create(**validate_data)
    #     obj = super().create(validated_data)
    #     return obj
    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None 
        return  reverse("product:detail", kwargs={'pk':obj.pk}, request=request)       #f'product/detail-product/{obj}'    
        
    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
    
        
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        elif not isinstance(obj, Product):
            return None
        return obj.get_discount    