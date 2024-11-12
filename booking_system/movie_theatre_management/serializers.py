from rest_framework import serializers
from .models import *

class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = ['theatre_id', 'theatre_name', 'theatre_location']

class ScreenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Screen
        fields = ['screen_id', 'screen_number']

class ShowDetailSerializer(serializers.ModelSerializer):
    show_time = serializers.TimeField(format='%I:%M %p', input_formats=['%I:%M %p'])
    
    class Meta:
        model = ShowDetail
        fields = ['show_id', 'show_date', 'show_time']

class MovieSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Movie
        fields = ['movie_id', 'movie_name', 'movie_genre', 'movie_language', 'theatre', 'screen', 'showdetail']

class MovieViewSerializer(serializers.ModelSerializer):

    theatre = TheatreSerializer()
    screen = ScreenSerializer()
    showdetail = ShowDetailSerializer()
    class Meta:
        model = Movie
        fields = ['movie_id', 'movie_name', 'movie_genre', 'movie_language', 'theatre', 'screen', 'showdetail']

