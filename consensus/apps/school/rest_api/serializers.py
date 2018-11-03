from rest_framework import serializers

from apps.school import models


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'full_name',
            'phone_number',
            'address',
            'country',
            'state',
            'city',
            'zip_code',
            'application_reviews_required',
            )
        model = models.School
