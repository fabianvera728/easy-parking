# Generated by Django 2.2.24 on 2021-10-08 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0009_alter_reservation_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
