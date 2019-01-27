from apps.application.models import Application
from apps.application.rest_api.serializers import ApplicationSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



class ApplicationView(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    ordering = 'id'
    ordering_fields = '__all__'
