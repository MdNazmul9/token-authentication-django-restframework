from django.db import models

# Create your models here.
class Post(models.Model):
    username = models.CharField(max_length=200)
    userID = models.CharField(max_length=200)
    roomID = models.CharField(max_length=200)

    def __str__(self):
        return self.roomID