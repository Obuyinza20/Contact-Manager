# Generated by Django 3.0.5 on 2023-03-01 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='owner',
            field=models.CharField(default='anonymous', max_length=200),
        ),
    ]
