from rest_framework import serializers

from apps.school import models


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.School


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Application


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Score


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Season


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Staff