# Generated by Django 3.2.8 on 2021-10-08 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parking_lots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('used_places', models.PositiveIntegerField(default=0)),
                ('remaining_places', models.PositiveIntegerField(default=0)),
                ('reserved_limit', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Place',
                'verbose_name_plural': 'Places',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=254)),
                ('verbose_name', models.TextField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('start_timestamp', models.DateTimeField(auto_now_add=True)),
                ('final_timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_reserved', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=False)),
                ('net_cost', models.FloatField(default=0)),
                ('is_paid', models.FloatField(default=False)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_lots.parking')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
            },
        ),
    ]
