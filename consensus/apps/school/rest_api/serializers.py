from rest_framework import serializers

from apps.school import models


class SchoolSerializer(serializers.ModelSerializer):
    #seasons = models.ForeignKey(Season, on_delete=models.CASCADE)

    class Meta:
        fields = (
            'id',
            'user_id',
            'full_name',
            'phone_number',
            'email',
            'grade',
            'address',
            'country',
            'state',
            'city',
            'zip_code',
            'application_reviews_required',
            )
        model = models.School
