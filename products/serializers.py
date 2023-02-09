from rest_framework import serializers
from products import models


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = '__all__'