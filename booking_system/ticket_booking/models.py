from django.db import models
from movie_theatre_management.models import Movie
from user_register.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AnonymousUser

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='loggedin_user', on_delete=models.CASCADE, blank=True)  
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_number = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], blank=False)
    status = models.CharField(max_length=50, choices=[('Booked', 'Booked'), ('Cancelled', 'Cancelled')])
    
    def __str__(self):
        return f"Seat no. {self.seat_number} is {self.status}"

    @staticmethod
    def is_seat_available(movie, seat_number):
        return not Booking.objects.filter(movie=movie, seat_number=seat_number, status="Booked").exists()

    def save(self, *args, **kwargs):
        if not self.user:
            if hasattr(self, 'request') and isinstance(self.request.user, CustomUser) and not isinstance(self.request.user, AnonymousUser):
                self.user = self.request.user
        super().save(*args, **kwargs)

    def cancel_booking(self):
        if self.status == 'Booked':
            self.status = 'Cancelled'
            self.save()
            return True
        return False
