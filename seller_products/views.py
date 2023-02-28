from rest_framework.viewsets import ModelViewSet

from utils import mixins
from . import serializers, models


class SellerProductViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    ACTION_SERIALIZERS = {
        'create':serializers.SellerProductCreateSerializer,
    }
    serializer_class = serializers.SellerProductSerializer
    queryset = models.Seller_Product.objects.select_related('seller', 'product')

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)
