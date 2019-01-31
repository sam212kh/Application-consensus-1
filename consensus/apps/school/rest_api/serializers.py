from rest_framework import serializers

from apps.school import models


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.School


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
