# Generated by Django 4.0.1 on 2022-01-24 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
