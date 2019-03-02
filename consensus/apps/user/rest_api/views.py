from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from djoser.serializers import UserSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from djoser.views import SetPasswordView as JoserSetPasswordView

from apps.user.models import User
from .serializers import SessionSerializer, UserSessionSerializer


class SessionView(viewsets.ViewSet):

    class SessionPermission(permissions.BasePermission):
        """ custom class to check permissions for sessions """

        def has_permission(self, request, view):
            """ check request permissions """
            if request.method == 'POST' or request.method == 'PUT':
                return True
            return request.user.is_authenticated and request.user.is_active

    permission_classes = (SessionPermission,)
    serializer_class = SessionSerializer

    def get(self, request, *args, **kwargs):
        """ api to get current session """

        return Response(UserSessionSerializer(request.user, context={'request': request}).data)

    def put(self, request, *args, **kwargs):
        """ api to login """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.data)
        if not user:
            return Response({'reason': 'Username or password is incorrect'}, status=400)
        if not user.is_active:
            return Response({'reason': 'User is inactive'}, status=403)

        login(request, user)
        response = Response(UserSessionSerializer(user, context={'request': request}).data)
        return response

    def delete(self, request, *args, **kwargs):
        """ api to logout """

        user_id = request.user.id
        logout(request)
        response = Response({'id': user_id})
        return response

    def post(self, request, *args, **kwargs):
        VALID_USER_FIELDS = [f.name for f in User._meta.fields]
        DEFAULTS = {
            # you can define any defaults that you would like for the user, here
        }
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            user_data = {field: data for (field, data) in request.data.items() if field in VALID_USER_FIELDS}
            user_data.update(DEFAULTS)
            user = User.objects.create_user(
                **user_data
            )
            return Response(UserSerializer(instance=user).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    create = post  # this is a trick to show this view in api-root


class SetPasswordView(JoserSetPasswordView):
    def post(self, request, *args, **kwargs):
        return super(SetPasswordView, self).post(request)
