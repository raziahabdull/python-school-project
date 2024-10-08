# Generated by Django 5.0.7 on 2024-07-22 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=40)),
                ('course_id', models.CharField(max_length=20)),
                ('course_descirption', models.TextField()),
                ('class_hours', models.PositiveSmallIntegerField()),
                ('prerequisites', models.CharField(max_length=80)),
                ('assessment_requirements', models.DateField()),
                ('school_term', models.PositiveSmallIntegerField()),
                ('course_capacity', models.PositiveSmallIntegerField()),
                ('grade_level', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
