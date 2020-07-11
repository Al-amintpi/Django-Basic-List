from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import QueryApp
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProjectApp.urls')),
    path('', include('QueryApp.urls')),
    #drf
    path('crud/', include(('crudapp.urls', 'crudapp'), namespace='crud_root_app_url')),
    path('api-auth/', include('rest_framework.urls')),
]


handler404 = QueryApp.views.handler404
handler500 = QueryApp.views.handler500


if settings.DEBUG:  # if local server
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
