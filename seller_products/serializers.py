from rest_framework import serializers
from products import serializers as product_serializers
from . import models


class SellerProductSerializer(serializers.ModelSerializer):
    product = product_serializers.ProductSerializer()

    class Meta:
        model = models.Seller_Product
        fields = '__all__'