from rest_framework import serializers

from apps.score import models

class ScoreSerializer(serializers.ModelSerializer):
    #school_id = SchoolSerializer()
    class Meta:
        fields = (
            'id',
            'school_id',
            'application_id',
            'staff_id',
            'first_name',
            'last_name',
            'score_date',
            'score',
            )
        model = models.Score
