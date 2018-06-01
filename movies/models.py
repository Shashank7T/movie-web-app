from django.db import models


# Create your models here.
class Movies(models.Model):
    Name = models.CharField(max_length=50)
    Picture = models.URLField(max_length=500)
    Rating = models.IntegerField()
    Notes = models.TextField(max_length=1000)

    def __str__(self):
        return self.Name