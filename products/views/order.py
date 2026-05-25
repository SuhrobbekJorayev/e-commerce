from rest_framework import viewsets
from products.models import Order
from products.serializers import OrderSerializer
from products.permissions import IsOwnerOrReadOnly


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
