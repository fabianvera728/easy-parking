# Generated by Django 2.2.24 on 2021-10-06 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=254)),
                ('verbose_name', models.TextField(max_length=50)),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
        ),
    ]
