# Generated by Django 5.0.8 on 2024-08-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_remove_reservation_data_reservation_party_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]