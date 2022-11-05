from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from BFDESK import settings

urlpatterns = [
                  path('', include('dashboard.urls')),
                  path('authentication', include('django.contrib.auth.urls')),
                  path('authentication/', include('authentication.urls')),
                  path('clients/', include('clients.urls')),
                  path('appointments/', include('appointments.urls')),
                  path('record_reporting/', include('record_reporting.urls')),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
