# Generated by Django 2.2.4 on 2020-03-25 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minor', '0008_auto_20200325_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='srs',
            field=models.FileField(blank=True, default='settings.MEDIA_ROOT/documents/default.txt', upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='synopsis',
            field=models.FileField(blank=True, default='settings.MEDIA_ROOT/documents/default.txt', upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='wbs',
            field=models.FileField(blank=True, default='settings.MEDIA_ROOT/documents/default.txt', upload_to='documents/'),
        ),
    ]