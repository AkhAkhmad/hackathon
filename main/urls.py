from django.contrib.auth import views as v
from django.urls import path

from . import views

urlpatterns = [
    path('', views.func, name='base'),
    path('login/', v.LoginView.as_view(next_page='base'), name='login'),
    path('logout/', v.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('password-reset/', v.PasswordResetView.as_view(template_name='registration/password_reset.html',
                                                        html_email_template_name='registration/password_reset_email.html'),
         name='password-reset'),
    path('password-reset/done/', v.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', v.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/', v.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]
