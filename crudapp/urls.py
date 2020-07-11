from django.contrib import admin
from django.urls import path, include
from crudapp.views import *
from.import views


urlpatterns = [
    path('api/', include(('crudapp.api.urls', 'crudapp'), namespace='crudapp_url')),
    path('drf_url/', views.get_drf_view, name="test_drf_url"),
]