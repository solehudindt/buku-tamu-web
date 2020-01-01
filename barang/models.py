from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

# Create your models here.
class AdmBarang(models.Model):
    nama        = models.CharField(max_length=35)
    angkatan    = models.IntegerField(
                            validators=[MinValueValidator(2010),
                            max_value_current_year]
                            )
    barang      = models.CharField(max_length=20)
    tanggal     = models.DateField(auto_now=False, auto_now_add=True)
    jenis        = models.CharField(max_length=10, choices=[
                                                    ('peminjaman', 'Peminjaman'),
                                                    ('penitipan', 'Penitipan')
                                                ]
                )
    at_camp     = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.nama, self.barang)
    