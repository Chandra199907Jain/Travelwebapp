# Generated by Django 2.2.24 on 2021-06-15 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='mobile',
        ),
    ]
