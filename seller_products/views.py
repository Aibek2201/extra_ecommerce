from rest_framework.viewsets import ModelViewSet

from utils import mixins
from . import serializers, models, permissions


class SellerProductViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    ACTION_SERIALIZERS = {
        'create':serializers.SellerProductCreateSerializer,
    }
    serializer_class = serializers.SellerProductSerializer
    queryset = models.Seller_Product.objects.select_related('seller', 'product')
    permission_classes = permissions.IsSeller,

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)
