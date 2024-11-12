from rest_framework import serializers
from .models import Booking
from movie_theatre_management.serializers import MovieViewSerializer
from user_register.serializers import UserSerializer

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['booking_id', 'user', 'movie', 'seat_number', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context['request'].method == 'PUT':
            self.fields['movie'].read_only = True
            self.fields['seat_number'].read_only = True    
    
    def validate(self, data):
        if self.context['request'].method == 'PUT':
            if self.instance and 'status' in data:
                if data['status'] == 'Booked':
                    raise serializers.ValidationError("You cannot set the status back to 'Booked'.")
        if self.instance is None and data['status'] == 'Booked':
            movie = data['movie']
            seat_number = data['seat_number']
            if Booking.objects.filter(movie=movie, seat_number=seat_number, status="Booked").exists():
                raise serializers.ValidationError("This seat is already booked!")
        return data

    def update(self, instance, validated_data):
        status = validated_data.get('status', None)
        if status is not None:
            instance.status = status
            instance.save()
        return instance
    
       
class BookingViewSerializer(serializers.ModelSerializer):
    movie = MovieViewSerializer()
    user = UserSerializer()

    class Meta:
        model = Booking
        fields = ['booking_id','user', 'movie', 'seat_number', 'status']



