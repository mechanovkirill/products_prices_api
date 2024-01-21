from rest_framework import permissions, viewsets
from .serializers import ProductSerializer
from .services import get_products


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows get current product prices.
    """
    queryset = get_products()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
