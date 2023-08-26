from django.urls import path
from . import views
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)
from django.urls import reverse_lazy
urlpatterns = [
    #--------------------------------ManageUsers-------------------------------------------#
    path('SingUp/',views.Accounts.SingUpPages,name="SingUp"),
    path('Login/',LoginView.as_view(template_name='accounts/login.html'),name='Login'),
    path("Logout/",LogoutView.as_view(template_name='Home.html'),name='Logout'),
    path("Profile/",views.Accounts.PageProfile,name="Profile"),
    path("EditProfile/",views.Accounts.PageEditProfile,name="EditProfile"),
    path("Delete/",views.Accounts.PageDeleteAccount,name="Delete"),
    
    #--------------------------------ManagePassword-------------------------------------------#
    path('password/', PasswordChangeView.as_view(template_name='accounts/password/password_change.html',success_url=reverse_lazy('password_change_done')), name='password_change'),
    path('password/done/', PasswordChangeDoneView.as_view(template_name='accounts/password/password_done.html'), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
