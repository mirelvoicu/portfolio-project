from django.db import models

# Create your models here.

class Job(models.Model):

    image=models.ImageField(upload_to='images/', blank=True)
    title =models.CharField(max_length=2000)

    def __str__(self):
        return self.title
