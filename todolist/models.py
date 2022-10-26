from django.db import models

# Create your models here.
class todo (models.Model):
     text=models.models.CharField( max_length=50)
     complete=models.BooleanField(default=False)
     
     
     def __str__(self):
         return self.text
     