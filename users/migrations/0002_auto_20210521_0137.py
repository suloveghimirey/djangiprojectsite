# Generated by Django 2.2.16 on 2021-05-21 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_nuber',
            field=models.CharField(max_length=10),
        ),
    ]
