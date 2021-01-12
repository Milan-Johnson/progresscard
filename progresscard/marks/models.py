from django.db import models

# Create your models here.

class studentmarks(models.Model):

    user = models.CharField(max_length=50)
    malayalam = models.SmallIntegerField()
    englih = models.SmallIntegerField()
    hindi = models.SmallIntegerField()
    maths = models.SmallIntegerField()
    science = models.SmallIntegerField()
    socialscience = models.SmallIntegerField()
    