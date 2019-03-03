from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from apps.school.rest_api.views import SchoolView, ApplicationView, ScoreView, SeasonView, StaffView

SCHOOL_BASE_ENDPOINT = 'school/(?P<_school_pk>[0-9]+)'
SEASON_BASE_ENDPOINT = 'season/(?P<_season_pk>[0-9]+)'
APPLICATION_BASE_ENDPOINT = 'application/(?P<_application_pk>[0-9]+)'

rest_router = routers.DefaultRouter()
rest_router.trailing_slash = "/?"  # added to support both / and slashless
rest_router.register(r'school', SchoolView)
rest_router.register(r'{}/staff'.format(SCHOOL_BASE_ENDPOINT), StaffView)
rest_router.register(r'{}/season'.format(SCHOOL_BASE_ENDPOINT), SeasonView)
rest_router.register(r'{}/application'.format(SEASON_BASE_ENDPOINT), ApplicationView)
rest_router.register(r'{}/score'.format(APPLICATION_BASE_ENDPOINT), ScoreView)



app_name = 'school'
urlpatterns = [
    path('', include(rest_router.urls)),
]
