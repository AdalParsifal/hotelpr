# Generated by Django 5.0.6 on 2024-09-29 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelpacific', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitacion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='habitaciones/'),
        ),
    ]
