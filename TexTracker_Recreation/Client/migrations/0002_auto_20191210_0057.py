# Generated by Django 2.2.5 on 2019-12-09 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='client_firstname',
        ),
        migrations.RemoveField(
            model_name='client',
            name='client_lastname',
        ),
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
    ]
