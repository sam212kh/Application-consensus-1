from django.urls import path, include
from rest_framework import routers

from apps.school.rest_api.views import SchoolView, ApplicationView, ScoreView, SeasonView, StaffView

rest_router = routers.DefaultRouter()
rest_router.trailing_slash = "/?"  # added to support both / and slashless
rest_router.register(r'school', SchoolView)
rest_router.register(r'application', ApplicationView)
rest_router.register(r'score', ScoreView)
rest_router.register(r'season', SeasonView)
rest_router.register(r'staff', StaffView)




app_name = 'school'
urlpatterns = [
    path('', include(rest_router.urls)),
]


