from django.urls import include, path
from rest_framework import routers

from apps.user.rest_api.views import SessionView, SetPasswordView

rest_router = routers.DefaultRouter()
rest_router.trailing_slash = "/?"  # added to support both / and slashless
rest_router.register(r'session', SessionView, base_name='session')

app_name = 'user'
urlpatterns = [
    path('', include(rest_router.urls)),
    path('me/password', SetPasswordView.as_view()),
]
