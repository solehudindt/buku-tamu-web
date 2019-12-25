# Generated by Django 2.2.3 on 2019-12-25 10:48

import django.core.validators
from django.db import migrations, models
import kunjungan.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pengunjung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('angkatan', models.IntegerField(validators=[django.core.validators.MinValueValidator(2010), kunjungan.models.max_value_current_year])),
                ('keterangan', models.TextField()),
            ],
        ),
    ]
