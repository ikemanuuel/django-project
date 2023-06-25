from rest_framework import generics
from .models import Residents
from .serializers import ResidentsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
class ResidentsListCreateView(generics.ListCreateAPIView):
    queryset = Residents.objects.all()
    serializer_class = ResidentsSerializer


class ResidentsListView(generics.ListAPIView):
    queryset = Residents.objects.all()
    serializer_class = ResidentsSerializer

class ResidentsDelete(APIView):
    def delete(self, request, resident_id):
        try:
            resident = Residents.objects.get(id=resident_id)
            
            resident.delete()  # Delete the property
          
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Residents.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)