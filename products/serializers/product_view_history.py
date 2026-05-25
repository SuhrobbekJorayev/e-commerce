from rest_framework import serializers
from products.models import ProductViewHistory


class ProductViewHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductViewHistory
        fields = '__all__'
