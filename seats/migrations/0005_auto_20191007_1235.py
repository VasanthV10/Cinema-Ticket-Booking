# Generated by Django 2.2.6 on 2019-10-07 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seats', '0004_auto_20191007_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='noofseats',
            field=models.IntegerField(),
        ),
    ]
