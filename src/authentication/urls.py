from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

app_name = 'authentication'

urlpatterns = [
    path('password_reset_sent/', views.password_reset_sent, name="password_reset_sent"),
    path('log_in/', views.login_user, name="log_in"),
    path('signup/', views.signup_user, name="signup"),
    path('logout/', views.logout_user, name="logout"),
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='authentication/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='authentication/password_reset_complete.html'),
         name='password_reset_complete'),

]
