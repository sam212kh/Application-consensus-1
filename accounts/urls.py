from django.contrib import admin
from django.urls import path, include
from accounts import views as account_views
from django.contrib.auth import logout

urlpatterns = [
    path('login/', account_views.MyLoginView.as_view(), name='login'),
    path('dashboard/', account_views.DashboardView.as_view(), name='dashboard'),
    path('staff/', account_views.StaffView.as_view(), name='staff'),
    path('student/', account_views.StudentView.as_view(), name='student'),
    path('logout/', account_views.Logout, name='logout'),
]
