from account.views import register, user_follow
from os import name
from django.contrib.auth import views
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView
from django.shortcuts import redirect
from django.urls import path,reverse_lazy
from  django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views
app_name='account'
urlpatterns=[
    path('login/',auth_views.LoginView.as_view(redirect_authenticated_user=True),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('password_change/',auth_views.PasswordChangeView.as_view(
        success_url=reverse_lazy('account:password_change_done')
    ),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(
            success_url=reverse_lazy('account:password_reset')

    ),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
                    success_url=reverse_lazy('account:password_reset_confirm')

    ),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('register/',views.register,name='register'),
    path('edit/',views.edit,name='edit'),
    path('users/',views.user_list,name='user_list'),
    path('users/follow/',views.user_follow,name='user_follow'),
    path('users/<username>/',views.user_detail,name='user_detail'),
    path('',views.dashboard,name='dashboard'),
    
]