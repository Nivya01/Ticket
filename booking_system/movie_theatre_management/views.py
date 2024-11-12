from rest_framework import viewsets
from .models import *
from.serializers import *
from rest_framework.permissions import IsAuthenticated
from user_register.permissions import *

class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MovieSerializer
        if self.request.method == 'PUT':
            return MovieSerializer
        if self.request.method == 'DELETE':
            return MovieSerializer 
        return MovieViewSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class TheatreViewset(viewsets.ModelViewSet):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class ScreenViewset(viewsets.ModelViewSet):
    queryset = Screen.objects.all()
    serializer_class = ScreenSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class ShowDetailViewset(viewsets.ModelViewSet):
    queryset = ShowDetail.objects.all()
    serializer_class = ShowDetailSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

