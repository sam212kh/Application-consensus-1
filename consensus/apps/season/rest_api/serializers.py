from rest_framework import serializers

from apps.season import models
from apps.school.rest_api.serializers import SchoolSerializer

class SeasonSerializer(serializers.ModelSerializer):
    #school_id = SchoolSerializer()
    class Meta:
        fields = (
            'id',
            'school_id',
            'full_name',
            'kind',
            'start_date',
            'end_date',
            'info',
            )
        model = models.Season
