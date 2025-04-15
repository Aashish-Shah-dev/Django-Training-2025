from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ecom.api.urls', namespace='api')),

 ]

urlpatterns +=[
    path('api/token/', TokenObtainPairView.as_view(),
name='token_obtain_pair'),
    path('api/token/refresh/',TokenObtainPairView.as_view(),
name='token_refresh'),
]
   
