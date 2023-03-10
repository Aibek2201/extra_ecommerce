# Generated by Django 4.1.6 on 2023-02-15 20:20

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]
