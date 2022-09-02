from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from online_store.api.reports import monthly_report
from online_store.api.serializers import ProductSerializer, OrderSerializer, ReportEntrySerializer, \
    ReportParamsSerializer
from online_store.products.models import Product, Order


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-date')
    serializer_class = OrderSerializer


class MonthlyReportAPIView(APIView):
    def get(self, request):
        params_serializer = ReportParamsSerializer(data=request.GET)
        params_serializer.is_valid(raise_exception=True)
        params = params_serializer.save()

        data = monthly_report(params)
        serializer = ReportEntrySerializer(instance=data, many=True)

        return Response(data=serializer.data)
