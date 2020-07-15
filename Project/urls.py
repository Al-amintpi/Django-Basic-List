from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import QueryApp
from django.conf.urls import handler404, handler500

#translate
from django.conf.urls.i18n import i18n_patterns 
from django.utils.translation import gettext_lazy as _



urlpatterns = [
    path('admin/', admin.site.urls),
	path('i18n/', include('django.conf.urls.i18n')),
    path('', include('ProjectApp.urls')),
    path('', include('QueryApp.urls')),
    #drf
    path('crud/', include(('crudapp.urls', 'crudapp'), namespace='crud_root_app_url')),
    path('api-auth/', include('rest_framework.urls')),
    #login-singup ajax
    path('withoutajax/', include('withoutajax.urls')),
    path('', include('bothajax.urls'))
    
]

urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('', include('base.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = QueryApp.views.handler404
handler500 = QueryApp.views.handler500


if settings.DEBUG:  # if local server
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
