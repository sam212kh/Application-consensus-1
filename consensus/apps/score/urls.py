from django.urls import path, include
from rest_framework import routers

from apps.score.rest_api.views import ScoreView

rest_router = routers.DefaultRouter()
rest_router.trailing_slash = "/?"  # added to support both / and slashless
rest_router.register(r'score', ScoreView)




app_name = 'score'
urlpatterns = [
    path('', include(rest_router.urls)),
]
