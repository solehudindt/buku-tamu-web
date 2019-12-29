from django.db import models

# Create your models here.
class Peminjaman(models.Model):
    nama    = models.CharField(max_length=35)
    barang  = models.CharField(max_length=20)
    tanggal = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.nama, self.tanggal)