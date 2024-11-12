from django.db import models
 
class Theatre(models.Model):
    theatre_id = models.AutoField(primary_key=True)
    theatre_name = models.CharField(max_length=50)
    theatre_location = models.CharField(max_length=100)

    def __str__(self):
        return f"Theatre {self.theatre_name}"

class Screen(models.Model):
    screen_id = models.AutoField(primary_key=True)
    screen_number = models.IntegerField()

    def __str__ (self):
        return f"Screen {self.screen_number}"

class ShowDetail(models.Model):
    show_id = models.AutoField(primary_key=True)
    show_date = models.DateField()
    show_time = models.TimeField()

    def __str__ (self):
        return f"Show {self.show_id} at {self.show_time.strftime('%I:%M %p')}"
            
class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length= 50)
    movie_genre = models.CharField(max_length=30)
    movie_language = models.CharField(max_length=10)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)  
    showdetail = models.ForeignKey(ShowDetail, on_delete=models.CASCADE)
    
    def __str__ (self):  
        return f"Movie {self.movie_name}"   

    
