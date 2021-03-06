# Generated by Django 2.2.4 on 2020-04-16 12:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minor', '0014_auto_20200409_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultyinfo',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets are allowed')]),
        ),
        migrations.AlterField(
            model_name='groupinfo',
            name='member_1_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets are allowed')]),
        ),
        migrations.AlterField(
            model_name='groupinfo',
            name='member_2_name',
            field=models.CharField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets are allowed')]),
        ),
        migrations.AlterField(
            model_name='groupinfo',
            name='member_3_name',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets are allowed')]),
        ),
        migrations.AlterField(
            model_name='headofdepartment',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabets are allowed')]),
        ),
    ]
