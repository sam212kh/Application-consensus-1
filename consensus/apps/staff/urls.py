from django.urls import path, include
from rest_framework import routers

from apps.staff.rest_api.views import StaffView

rest_router = routers.DefaultRouter()
rest_router.trailing_slash = "/?"  # added to support both / and slashless
rest_router.register(r'staff', StaffView)




app_name = 'staff'
urlpatterns = [
    path('', include(rest_router.urls)),
]
