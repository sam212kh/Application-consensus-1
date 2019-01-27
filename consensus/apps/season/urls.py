from django.urls import path, include
from rest_framework import routers

from apps.season.rest_api.views import SeasonView

rest_router = routers.DefaultRouter()
rest_router.trailing_slash = "/?"  # added to support both / and slashless
rest_router.register(r'season', SeasonView)




app_name = 'season'
urlpatterns = [
    path('', include(rest_router.urls)),
]
