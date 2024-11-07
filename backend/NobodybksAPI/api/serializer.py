from rest_framework import serializers
from product.validators import validators_unique_product_name

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product:detail', lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField(validators = [validators_unique_product_name])


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    has_perms = serializers.BooleanField(read_only=True)
    #number = serializers.CharField(read_only=True)
    user_product = serializers.SerializerMethodField(read_only=True)
    
    def get_user_product(self, obj):
        user = obj 
        request = self.context.get('request')
        product = user.product_set.all()
        return ProductInlineSerializer(product, many=True, context={'request' : request}).data