from django.db.models import Min, Q
from rest_framework.viewsets import ModelViewSet

from utils import mixins
from products import models, serializers, permissions


class ProductImageViewSet(ModelViewSet):
    serializer_class = serializers.ProductImageSerializer
    queryset = models.Product.objects.all()
    permission_classes = permissions.IsAdminOrReadOnly,


class ProductViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    ACTION_SERIALIZERS = {
        'retrieve': serializers.RetrieveProductSerializer,
    }
    permission_classes = permissions.IsAdminOrReadOnly,
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.annotate(
        min_amount=Min('seller_products__amount', filter=Q(seller_products__is_active=True))
    )


