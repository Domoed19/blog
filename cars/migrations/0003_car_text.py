# Generated by Django 4.0.6 on 2022-08-18 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='text',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]