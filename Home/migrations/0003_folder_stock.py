# Generated by Django 4.0.2 on 2023-06-27 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]