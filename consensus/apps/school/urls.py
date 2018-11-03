from django.urls import path, include
from rest_framework import routers

from apps.school.rest_api.views import SchoolView

rest_router = routers.DefaultRouter()
rest_router.trailing_slash = "/?"  # added to support both / and slashless
rest_router.register(r'school', SchoolView)

app_name = 'school'
urlpatterns = [
    path('', include(rest_router.urls)),
]
