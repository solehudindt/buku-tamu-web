# Generated by Django 2.2.3 on 2019-12-29 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peminjaman',
            name='tipe',
        ),
        migrations.AlterField(
            model_name='peminjaman',
            name='tanggal',
            field=models.DateField(),
        ),
    ]