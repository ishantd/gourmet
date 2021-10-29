from accounts import views

from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('logout/', views.Logout, name='logout'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/reset_password/forgotpassword.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/reset_password/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/reset_password/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/reset_password/password_reset_done.html"), 
        name="password_reset_complete"),
]
