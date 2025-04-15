from django.urls import path , include
from rest_framework.routers import DefaultRouter
from ecom import views
from ecom.views import ProductViewset, CouponAPIView

app_name = 'ecom'
router = DefaultRouter()
router.register(r'products',ProductViewset)

urlpatterns = [
    path('coupons/', views.CouponAPIView.as_view(), name='CouponAPIView'),
    path('',include(router.urls)),
 ]