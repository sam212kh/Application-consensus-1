from django.contrib import admin
from django.urls import path, include, re_path
from accounts import views as account_views
from django.contrib.auth import logout

urlpatterns = [
    path('login/', account_views.MyLoginView.as_view(), name='login'),
    path('school-signup/', account_views.SchoolSignup.as_view(), name='school-signup'),
    path('dashboard/', account_views.DashboardView.as_view(), name='dashboard'),
    path('command/', account_views.CommandExecView.as_view(), name='command'),
    path('staff/', account_views.StaffView.as_view(), name='staff'),
    re_path('staff/(?P<pk>\d+)/edit/$', account_views.StaffEditView.as_view(), name='staff-edit'),
    re_path('batch/(?P<pk>\d+)/students/$', account_views.StudentView.as_view(), name='student'),
    path('batch/', account_views.BatchView.as_view(), name='batch'),
    path('upload/applications/', account_views.UploadApplications.as_view(), name='application-upload'),
    path('applications/', account_views.Applications.as_view(), name='applications'),
    path('logout/', account_views.Logout, name='logout'),
]
