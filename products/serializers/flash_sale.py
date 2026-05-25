from rest_framework import serializers
from products.models import FlashSale


class FlashSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashSale
        fields = ['id', 'product', 'discount_percentage', 'start_time', 'end_time']
