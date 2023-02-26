from rest_framework.viewsets import ModelViewSet

from . import serializers, models


class SellerProductViewSet(ModelViewSet):
    serializer_class = serializers.SellerProductSerializer
    queryset = models.Seller_Product.objects.select_related('seller', 'product')
