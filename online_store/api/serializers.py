from rest_framework import serializers

from online_store.api.common.nested_serializer import WritableNestedModelSerializer
from online_store.api.reports import ReportParams
from online_store.products.models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price']


class OrderSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=False, read_only=False)

    class Meta:
        model = Order
        fields = ['id', 'date', 'products']


class ReportEntrySerializer(serializers.Serializer):
    value = serializers.DecimalField(
        max_digits=15,
        decimal_places=2,
    )
    count = serializers.IntegerField()


class ReportParamsSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def create(self, validated_data):
        return ReportParams(**validated_data)

