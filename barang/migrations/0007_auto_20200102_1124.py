# Generated by Django 2.2.3 on 2020-01-02 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0006_auto_20200101_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admbarang',
            old_name='at_camp',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='admbarang',
            name='jenis',
            field=models.CharField(choices=[('peminjaman', 'Peminjaman'), ('penitipan', 'Penitipan')], default='peminjaman', max_length=10),
        ),
    ]
