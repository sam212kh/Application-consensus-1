from rest_framework import serializers

from apps.school import models


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'owner',
            'full_name',
            'email',
            'grade',
            'phone_number',
            'address',
            'country',
            'state',
            'city',
            'zip_code',
            'application_reviews_required',
        )
        model = models.School


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'school',
            'first_name',
            'last_name',
            'birth_date',
            'gender',
            'phone_number',
            'email',
            'info',
            'educational_info',
            'score',
            'created_date',
            'status'
        )
        model = models.Application


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'application',
            'staff',
            'first_name',
            'last_name',
            'score_date',
            'score',
        )
        model = models.Score


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'school',
            'full_name',
            'kind',
            'start_date',
            'end_date',
            'info',
        )
        model = models.Season


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'school',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'user_name',
            )
        model = models.Staff