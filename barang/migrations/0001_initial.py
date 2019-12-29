# Generated by Django 2.2.3 on 2019-12-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peminjaman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=35)),
                ('barang', models.CharField(max_length=20)),
                ('tipe', models.CharField(choices=[('peminjaman', 'Peminjaman'), ('pengembalian', 'Pengembalian')], max_length=50)),
                ('tanggal', models.DateField(auto_now=True)),
            ],
        ),
    ]