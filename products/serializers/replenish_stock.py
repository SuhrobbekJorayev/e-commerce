from rest_framework import serializers


class ReplenishStockSerializer(serializers.Serializer):
    amount = serializers.IntegerField(min_value=1)
