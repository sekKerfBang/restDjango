from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from .validators import validators_unique_product_name
from api.serializer import UserPublicSerializer


class ProductSerializers(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    #Premiere methode pour inserer de l'url a un champs depuis le serializer
    #url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product:detail', lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField(validators = [validators_unique_product_name])
    owner = serializers.SerializerMethodField(read_only=True)
    #user_name = serializers.CharField(source='user.username', read_only=True)
    # Seconde methode de relation ou related field permettant de lier n'import quel table a un serializer
    #owner = UserPublicSerializer(source='user', read_only=True)
    class Meta: 
        model = Product 
        fields = ( 'owner', 'email', 'url', 'pk', 'name', 'content', 'price', 'my_discount', 'public')
        
       
    def get_owner(self, obj):
        return { 'username' : obj.user.username, 'id' : obj.user.pk }   
    
       # Premiere methode de validation personnaliser avec le serializer  
    # def validate_name(self, value):
    #     qs = Product.objects.filter(name__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"Le produit {value} existe daja dans la base de donnee ")
    #     return value    
    # def create(self, validated_data):
    #     print(validated_data)
    #     email = validated_data.pop('email')
    #     print(email)
    #     print(validated_data)
    #     #return Product.objects.create(**validate_data)
    #     obj = super().create(validated_data)
    #     return obj
    # La methode permettant de lire l'url 
    # def get_url(self, obj):
    #     request = self.context.get('request')
    #     if request is None:
    #         return None 
    #     return  reverse("product:detail", kwargs={'pk':obj.pk}, request=request)       #f'product/detail-product/{obj}'    
        
    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
    
        
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        elif not isinstance(obj, Product):
            return None
        return obj.get_discount    