from django.contrib import admin
from django.urls import path, include
from .views import PersonViewSet
from.import views
from rest_framework.routers import DefaultRouter, SimpleRouter 

router = DefaultRouter()
router.register('Person', PersonViewSet, basename='router_register_crudapp')



urlpatterns = [
       path('api1/', include((router.urls, 'crudapp'), namespace='api_folder_url')),
]