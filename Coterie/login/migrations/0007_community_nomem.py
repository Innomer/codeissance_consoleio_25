# Generated by Django 4.1.1 on 2022-09-23 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_community'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='noMem',
            field=models.IntegerField(null=True),
        ),
    ]