from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters as drf_filters
from rest_framework.decorators import action

class BookingViewset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookingSerializer
        if self.request.method == 'PUT':
            return BookingSerializer
        if self.request.method == 'DELETE':
            return BookingSerializer 
        return BookingViewSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [drf_filters.SearchFilter]
    search_fields = ['user__username', 'user__email', 'movie__movie_genre', 'movie__movie_name', 'movie__movie_language', 'movie__theatre__theatre_name', 'movie__theatre__theatre_location', 'movie__showdetail__show_date', 'movie__showdetail__show_time',]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def cancel_booking(self, request, pk=None):
        booking = self.get_object()
        if booking.status == 'Booked':
            booking.status = 'Cancelled'
            booking.save()
            return Response({"message": "Booking canceled successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Booking is already canceled or You are not booking this seat"}, status=status.HTTP_400_BAD_REQUEST)
        
# /booking/?search=<keyword>

