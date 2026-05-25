from django_filters import rest_framework as django_filters
from products.models import FlashSale


class FlashSaleFilter(django_filters.FilterSet):
    min_discount = django_filters.NumberFilter(field_name='discount_percentage', lookup_expr='gte')
    max_discount = django_filters.NumberFilter(field_name='discount_percentage', lookup_expr='lte')

    class Meta:
        model = FlashSale
        fields = ['product']
