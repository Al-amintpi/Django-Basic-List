from django.contrib import admin
from django.urls import path
from.import views
from django.contrib.auth import views as auth_views

urlpatterns = [
		path('login/', views.get_login_view, name="login"),
		path('logout/', views.get_logout_view, name="logout"),
		path('register/', views.get_register_view, name="register"),
		path('change-password/', auth_views.PasswordChangeView.as_view(template_name="registration/password_change_form.html"),name='password_change'),
		path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
		
		path('password/reset/',auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),name='password_reset'),
		path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
		path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
		path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_change_done.html"), name="password_reset_complete")
    

    
]