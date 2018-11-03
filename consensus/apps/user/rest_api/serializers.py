from django.contrib.auth.models import Permission, Group
from rest_framework import serializers

from consensus.apps.user.models import UserProfile, User
from consensus.consensus.helpers.utils import DynamicFieldsSerializerMixin

class NestedProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('birth_date', 'gender', 'avatar')
        read_only_fields = ('avatar',)


class PermissionSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename')


class NestedGroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')


class UserSessionSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    profile = NestedProfileSerializer()
    user_permissions = PermissionSerializer(read_only=True, many=True)
    groups = NestedGroupSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ("id", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff",
                  "is_active", "date_joined", "groups", "user_permissions", "profile")


class SessionSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=128, style={'input_type': 'password'})
    remember = serializers.BooleanField(initial=False, required=False)


class FreshSessionSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, required=True, style={'input_type': 'password'})

class UserSessionSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    profile = NestedProfileSerializer()
    user_permissions = PermissionSerializer(read_only=True, many=True)
    groups = NestedGroupSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ("id", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff",
                  "is_active", "date_joined", "groups", "user_permissions", "profile")


class FreshSessionSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, required=True, style={'input_type': 'password'})