# Generated by Django 4.1.4 on 2023-02-09 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='adults',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='booking',
            name='children',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='multi_station',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='oneway',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='roundtrip',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
