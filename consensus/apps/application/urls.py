from django.urls import path, include
from rest_framework import routers

from apps.application.rest_api.views import ApplicationView

rest_router = routers.DefaultRouter()
rest_router.trailing_slash = "/?"  # added to support both / and slashless
rest_router.register(r'application', ApplicationView)




app_name = 'application'
urlpatterns = [
    path('', include(rest_router.urls)),
]
