from django.contrib import admin
from django.urls import path
from.import views
from django.contrib.auth import views as auth_views

urlpatterns = [
		path('both_login/', views.get_login_view, name="both_login"),
		path('both_logout/', views.get_logout_view, name="both_logout"),
		path('both_register/', views.get_register_view, name="both_register"),
		path('change-password/', auth_views.PasswordChangeView.as_view(template_name="bothajax/password_change_form.html"),name='password_change'),
		path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
		
		path('password/reset/',auth_views.PasswordResetView.as_view(template_name="bothajax/password_reset_form.html"),name='password_reset'),
		path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
		path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="bothajax/password_reset_confirm.html"), name='password_reset_confirm'),
		path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="bothajax/password_change_done.html"), name="password_reset_complete"),

		path('forget_password_form/', views.forget_password_view, name='forget_password_form'),
		path('update_forget_password/<username>/<token>/', views.update_forget_password_view, name='update_forget_password'),
		path('password_reset/', views.password_reset_view, name="password_reset")
		

    
]