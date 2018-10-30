from datetime import timedelta

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from djoser.views import SetPasswordView as JoserSetPasswordView
from .serializers import SessionSerializer, UserSessionSerializer, FreshSessionSerializer


class SessionView(viewsets.ViewSet):

    class SessionPermission(permissions.BasePermission):
        """ custom class to check permissions for sessions """

        def has_permission(self, request, view):
            """ check request permissions """
            if request.method == 'POST':
                return True
            return request.user.is_authenticated and request.user.is_active

    permission_classes = (SessionPermission,)
    serializer_class = SessionSerializer

    def get(self, request, *args, **kwargs):
        """ api to get current session """

        return Response(UserSessionSerializer(request.user, context={'request': request}).data)

    def post(self, request, *args, **kwargs):
        """ api to login """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.data)
        if not user:
            return Response({'reason': 'Username or password is incorrect'}, status=400)
        if not user.is_active:
            return Response({'reason': 'User is inactive'}, status=403)

        login(request, user)
        fresh_expiry = settings.FRESH_AUTH_EXPIRY
        if isinstance(fresh_expiry, timedelta):
            fresh_expiry = fresh_expiry.total_seconds()
        response = Response(UserSessionSerializer(user, context={'request': request}).data)
        return self.fresh_response(response, fresh_expiry)

    def delete(self, request, *args, **kwargs):
        """ api to logout """

        user_id = request.user.id
        logout(request)
        response = Response({'id': user_id})
        if settings.FRESH_AUTH_KEY in request.COOKIES:
            response.delete_cookie(settings.FRESH_AUTH_KEY)
        return response

    create = post  # this is a trick to show this view in api-root


class SetPasswordView(JoserSetPasswordView):
    def post(self, request, *args, **kwargs):
        return super(SetPasswordView, self).post(request)
