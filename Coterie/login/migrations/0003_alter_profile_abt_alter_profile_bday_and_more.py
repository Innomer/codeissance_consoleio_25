# Generated by Django 4.1.1 on 2022-09-23 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_profile_email_profile_pw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='abt',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ed',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
