from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # average_rating = models.FloatField(default=0)
    class Meta:
        app_label = 'vidixerapp'
    # Add more fields as needed



class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])  # Rating from 0 to 5
    comment = models.TextField(blank=True, null=True)  # Optional comment from the client



class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='media/videos/')
    upload_date = models.DateTimeField(auto_now_add=True)
    # min_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # max_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Add more fields as needed

    def __str__(self):
        return self.title
    
    

class Proposal(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.ForeignKey(Rating, on_delete=models.SET_NULL, blank=True, null=True)
    # Add more fields as needed



