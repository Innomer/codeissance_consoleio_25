# Generated by Django 4.1.1 on 2022-09-23 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_profile_abt_alter_profile_bday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pp',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='streak',
            field=models.IntegerField(null=True),
        ),
    ]
