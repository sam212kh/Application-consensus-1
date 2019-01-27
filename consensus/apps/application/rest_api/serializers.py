from rest_framework import serializers

from apps.application import models

class ApplicationSerializer(serializers.ModelSerializer):
    #school_id = SchoolSerializer()
    class Meta:
        fields = (
            'id',
            'school_id',
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
