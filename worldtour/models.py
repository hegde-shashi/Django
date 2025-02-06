from django.db import models

# Create your models here.
class world(models.Model):
    origin_country = models.CharField(max_length=100)
    destination_country = models.CharField(max_length=100)
    number_of_days = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return ("ID: %s, Origin Country: %s, Destination Country: %s, Number of Days: %s, Price: %s" % (self.id, self.origin_country, self.destination_country, self.number_of_days, self.price))
