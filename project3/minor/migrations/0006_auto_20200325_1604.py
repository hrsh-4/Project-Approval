# Generated by Django 2.2.4 on 2020-03-25 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minor', '0005_auto_20200325_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='srs',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='project',
            name='synopsis',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='project',
            name='wbs',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]
