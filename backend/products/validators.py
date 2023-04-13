
from rest_framework import serializers
from .models import Product


# put validators on models rather than this kind of way.
def validate_title(self, value):
        print('validate_title function')
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name")
        return value