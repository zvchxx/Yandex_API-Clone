from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('superadmin/', include('admin.urls')), 
    path('user/', include('user.urls')), 
    path('branch/', include('branch.urls')), 
    path('courier/', include('courier.urls')), 
    path('restaurant/', include('restaurant.urls')),  
    path('product/', include('product.urls')),
    path('feedback/', include('feedback.urls')),
    path('basket/', include('basket.urls')),
    path('order/', include('order.urls')),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)