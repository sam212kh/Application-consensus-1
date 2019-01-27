from apps.season.models import Season
from apps.season.rest_api.serializers import SeasonSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



class SeasonView(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    ordering = 'id'
    ordering_fields = '__all__'
