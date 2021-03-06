# Generated by Django 2.2.3 on 2020-01-01 12:09

import barang.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0005_auto_20191230_0602'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmBarang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=35)),
                ('angkatan', models.IntegerField(validators=[django.core.validators.MinValueValidator(2010), barang.models.max_value_current_year])),
                ('barang', models.CharField(max_length=20)),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('jenis', models.CharField(choices=[('peminjaman', 'Peminjaman'), ('penitipan', 'Penitipan')], max_length=10)),
                ('at_camp', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Peminjaman',
        ),
    ]
