from rest_framework import serializers
from .models import Product, OrderItem , Order


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'price',
            'stock',
        )
    def validate_price(self, value):
        if value <= 0 :
            raise serializers.ValidationError(
                "Price must be greater then 0"
            )  
        return value  

    def validate_stock(self, value):
            if value <= 0 :
                raise serializers.ValidationError(
                    "Stock must be greater then 0"
                )  
            return value  