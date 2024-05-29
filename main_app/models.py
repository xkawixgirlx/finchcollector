from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    place = models.TextField(max_length=250)
    color = models.TextField(max_length=250)
    
    def __str__(self):
       return self.name, self.type, self.color