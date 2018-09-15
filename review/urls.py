from django.contrib import admin
from django.urls import path, include, re_path
from review import views as review_views
from django.contrib.auth import logout

urlpatterns = [
    path('application/submit', review_views.ApplicationView.as_view(), name='application-submit'),
    path('application/review', review_views.ReviewView.as_view(), name='application-review'),
    re_path('application/rate/(?P<pk>\d+)/$', review_views.ReviewDetailView.as_view(), name='application-rate'),
]
