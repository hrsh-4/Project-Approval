# Generated by Django 2.2.4 on 2020-04-09 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minor', '0012_auto_20200325_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='srs',
            field=models.FileField(blank=True, default='settings.MEDIA_ROOT/documents/default.txt', null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='synopsis',
            field=models.FileField(blank=True, default='settings.MEDIA_ROOT/documents/default.txt', null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='wbs',
            field=models.FileField(blank=True, default='settings.MEDIA_ROOT/documents/default.txt', null=True, upload_to='documents/'),
        ),
    ]
