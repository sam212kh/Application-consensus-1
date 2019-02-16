from rest_framework import serializers
from apps.school import models
from apps.school.models import Participation, School
import datetime


class SchoolSerializer(serializers.ModelSerializer):

    # Use this method for get current user
    def _user(self, obj):
        kwargs = getattr(self, '_kwargs', None)
        request = kwargs['context']['request']
        return request.user

    class Meta:
        fields = '__all__'
        model = models.School

    def create(self, validated_data):
        school = School.objects.create(**validated_data)
        Participation.objects.create(
            school=school,
            participant=self._user(self),
            participation_type=Participation.PARTICIPATION_OWNER,
            participation_date=datetime.datetime.now()
        )
        return school


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Staff


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Season


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Application


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Score
