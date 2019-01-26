from apps.school.models import School
from apps.school.rest_api.serializers import SchoolSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    ordering = 'id'
    ordering_fields = '__all__'

    def list(self, request, *args, **kwargs):
        queryset = School.objects.filter(user_id=self.request.user.id).all()
        response =  super().list(request, *args, **kwargs)
        newdict={
            'total_season_count': 0,
            'total_application_count':15,
            'total_staff_count':4,
            'total_score_count':7,
            'total_enrolled_count': 11,
            'seasons':
            {
                'id': 18,
                'full_name': "season_11",
                'application': 7,
                'scored': 4,
                'enrolled': 2
                }
        }
        newdict.update(response.data)
        return Response(newdict)
        custom_data = {
        'list_of_items': SchoolSerializer(queryset).data
        }
        custom_data.update({
            'total_season_count': 0,
            'total_application_count':15,
            'total_staff_count':4,
            'total_score_count':7,
            'total_enrolled_count': 11,
            'seasons':
            {
                'id': 18,
                'full_name': "season_11",
                'application': 7,
                'scored': 4,
                'enrolled': 2
                }
        })
        return Response(custom_data)

    def get_queryset(self):
        return School.objects.filter(user_id=self.request.user.id).only('id', 'full_name').all()





    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
