# Generated by Django 4.1.1 on 2022-09-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pp', models.ImageField(upload_to='')),
                ('username', models.CharField(blank=True, max_length=20)),
                ('fullname', models.CharField(blank=True, max_length=50)),
                ('ed', models.CharField(blank=True, max_length=40)),
                ('abt', models.TextField(blank=True, max_length=200)),
                ('bday', models.DateField()),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('career', models.CharField(blank=True, max_length=50, null=True)),
                ('interest', models.JSONField(default=list, null=True)),
                ('communities', models.JSONField(default=list, null=True)),
                ('streak', models.IntegerField()),
            ],
        ),
    ]