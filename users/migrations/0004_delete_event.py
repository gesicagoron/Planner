# Generated by Django 4.2.7 on 2024-01-14 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_event'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
    ]