# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='rate',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apartment',
            name='amenities',
            field=models.ManyToManyField(related_name='apartments', to='apartments.Amenity'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='building',
            field=models.ForeignKey(related_name='apartments', to='apartments.Building'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='apartment',
            field=models.ForeignKey(related_name='bookings', to='apartments.Apartment'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(related_name='bookings', to='apartments.Guest'),
        ),
    ]
