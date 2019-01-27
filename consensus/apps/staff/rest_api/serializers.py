from rest_framework import serializers

from apps.staff import models

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'school_id',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'user_name',
            )
        model = models.Staff
