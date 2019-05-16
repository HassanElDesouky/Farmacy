from django.db import models

# Create your models here.


class Medicine(models.Model):
    medicine_name = models.CharField(max_length=200)
    pharmacy_name = models.CharField(max_length=300)
    pharmacy_location = models.TextField()

    def __str__(self):
        return self.medicine_name + ' in ' + self.pharmacy_name + ' at ' + self.pharmacy_location