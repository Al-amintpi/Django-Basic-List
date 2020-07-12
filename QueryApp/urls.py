from django.contrib import admin
from django.urls import path, include
from QueryApp.views import *
from.import views

urlpatterns = [
		path('home_page/', views.index, name="home"),
		path('objects_temp_show/', views.get_objects_temp_show, name='objects_temp_show'),
		path('object_json_format/', views.get_object_json_format, name='object_json_format'),
		path('post_or_update/', views.get_post_or_update, name='post_or_update'),
		path('single_object/<int:id>/', views.get_single_object, name="single_object"),
		path('delete/<int:id>/', views.get_delete_view, name="delete"),
		
		path('photo_url/', views.get_photo, name="photo"),
		path('request_url/', views.get_request, name="request"),
		#export and import
		path('export_url/', views.export, name="export"),
		path('import_url/', views.importpackage, name="import"),
		path('export_url1/', views.export1, name="export1"),
		path('import_url1/', views.import1, name="import1"),
		path('import_export_show/', views.import_export, name="import_export"),
		#django pdf
		path('download_url/', views.download_view, name="download"),
		path('preview_url/', views.preview_view, name='preview'),
		path('pdf/', views.pdf, name="pdf_file"),
		

        
]

