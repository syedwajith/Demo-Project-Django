# Generated by Django 4.0.7 on 2022-12-09 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerdetails',
            name='Status',
            field=models.BooleanField(default=False),
        ),
    ]
