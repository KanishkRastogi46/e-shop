from rest_framework.serializers import ModelSerializer
from .models import User, Shop, Product, Discount

# Serializers
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'is_vendor')
        extra_kwargs = {'password': {'write_only': True}}

class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class DiscountSerializer(ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'