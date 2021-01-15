from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class marks(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    malayalam = models.SmallIntegerField()
    english = models.SmallIntegerField()
    hindi = models.SmallIntegerField()
    maths = models.SmallIntegerField()
    science = models.SmallIntegerField()
    socialscience = models.SmallIntegerField()
    