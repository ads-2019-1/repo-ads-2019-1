# Generated by Django 2.0.7 on 2019-06-04 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conquista', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conquista',
            name='valor',
            field=models.IntegerField(default=0),
        ),
    ]
