# Generated by Django 2.2.3 on 2019-10-11 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Outward', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outward',
            name='outward_uploaddocstatus',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
