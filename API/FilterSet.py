from .models import Property
from django_filters import rest_framework as filters

class PropertyFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    location = filters.CharFilter(field_name="location__location")
    class Meta:
        model = Property
        fields = ['location','property_type','featured','no_bathrooms','no_bedrooms','min_price','max_price']


