from django.db import models

# Create your models here.
class Monitor(models.Model):
    """This class create the table for temperature and humidity and stores the them in the database."""
    temp = models.FloatField(max_length=20, blank= False)
    hum = models.FloatField(max_length=20, blank=False)

    def __str__(self):
        return str(self.temp)


