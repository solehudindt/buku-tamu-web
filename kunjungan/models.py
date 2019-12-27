import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

def year_choices():
    return [(r,r) for r in range(2010, datetime.date.today().year+1)]

a = year_choices()

# Create your models here.
class Pengunjung(models.Model):
    nama		    = models.CharField(max_length=35)
    angkatan		= models.IntegerField(
                            validators=[MinValueValidator(2010), 
                            max_value_current_year],
                            choices=a)
    keterangan		= models.TextField()
    
    def __str__(self):
        return "{} - {}".format(self.nama, self.angkatan)