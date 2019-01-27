from apps.score.models import Score
from apps.score.rest_api.serializers import ScoreSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



class ScoreView(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    ordering = 'id'
    ordering_fields = '__all__'
