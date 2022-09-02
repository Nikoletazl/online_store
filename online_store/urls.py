
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from online_store.api.views import ProductViewSet, OrderViewSet, MonthlyReportAPIView

router = DefaultRouter()
router.register(r'api/products', ProductViewSet, basename='product')
router.register(r'api/orders', OrderViewSet, basename='order')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/stats', MonthlyReportAPIView.as_view(), name='report'),
]
