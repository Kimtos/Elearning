# Generated by Django 3.1.4 on 2021-01-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0041_auto_20210108_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='amount',
            field=models.FloatField(),
        ),
    ]
