# Generated by Django 4.1.4 on 2023-02-07 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_booking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]