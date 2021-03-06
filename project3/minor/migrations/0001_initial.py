# Generated by Django 2.2.4 on 2020-03-16 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(choices=[('CE', 'Civil Engineering'), ('CSE', 'Computer Science'), ('ECE', 'Electronics and Communication'), ('IT', 'Information Technology'), ('ME', 'Mechanical Engineering')], max_length=3)),
                ('contact', models.PositiveIntegerField(unique=True)),
                ('is_faculty', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('3', 'THIRD'), ('4', 'FOURTH')], max_length=6)),
                ('section', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4)], max_length=1)),
                ('department', models.CharField(choices=[('CE', 'Civil Engineering'), ('CSE', 'Computer Science'), ('ECE', 'Electronics and Communication'), ('IT', 'Information Technology'), ('ME', 'Mechanical Engineering')], max_length=3)),
                ('group_name', models.CharField(max_length=20, unique=True)),
                ('member_1_name', models.CharField(max_length=100)),
                ('member_1_enrollment', models.CharField(max_length=15, unique=True)),
                ('member_2_name', models.CharField(blank=True, max_length=100)),
                ('member_2_enrollment', models.CharField(blank=True, max_length=15, unique=True)),
                ('member_3_name', models.CharField(blank=True, max_length=100)),
                ('member_3_enrollment', models.CharField(blank=True, max_length=15, unique=True)),
                ('contact', models.PositiveIntegerField(unique=True)),
                ('is_group', models.BooleanField(default=True)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='minor.FacultyInfo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='No project choosen', max_length=300)),
                ('description', models.TextField(default='No description')),
                ('is_approved_by_mentor', models.BooleanField(default=False)),
                ('is_approved_by_HOD', models.BooleanField(default=False)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='minor.GroupInfo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HeadOfDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('CE', 'Civil Engineering'), ('CSE', 'Computer Science'), ('ECE', 'Electronics and Communication'), ('IT', 'Information Technology'), ('ME', 'Mechanical Engineering')], max_length=3)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.PositiveIntegerField()),
                ('is_HOD', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClassCoordinator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('3', 'THIRD'), ('4', 'FOURTH')], default=None, max_length=1)),
                ('section', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4)], max_length=1)),
                ('faculty', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='minor.FacultyInfo')),
            ],
        ),
    ]
