from django.contrib import admin
from django.urls import path, include
from accounts.views import ApiHomeView

from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # documentation urls
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('apartments.urls')),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

