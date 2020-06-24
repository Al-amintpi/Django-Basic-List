from django.contrib import admin
from django.urls import path, include
from ProjectApp.views import *
from ProjectApp.models import Article
from.import views
from ProjectApp.views import ArticledeleteView, ArticleHomeView, PostDetailsView,ArticleupdateView, UpdateView, ArticleCreateView
	

 
app_name = 'ProjectApp'

urlpatterns = [
    path('home_url/', ArticleHomeView.as_view()),
    path('detail_url/<int:pk>/', PostDetailsView.as_view(), name='detail'),
    # path('update_url/<int:pk>/', UpdateView.as_view(), name='updated'),
    path('create_url/', ArticleCreateView.as_view(), name="create"),
	#path('index/<int:id>/', views.get_index, name="index")
	path('staff_url/<int:id>/', views.staff_required_action, name="staff"),
	path('super_url/', views.superuser_required_action, name="super"),
	path('article_delete/<int:id>/',views.ArticledeleteView.as_view(), name="delete" ),
	path('article_update/<int:id>/', views.ArticleupdateView.as_view(), name='update'),
	#Manager
	path('manager_url/', views.get_manager, name="manager"),
]