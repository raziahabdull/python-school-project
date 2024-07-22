# Generated by Django 5.0.7 on 2024-07-22 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassDuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=40)),
                ('class_id', models.PositiveSmallIntegerField()),
                ('course_descirption', models.CharField(max_length=20)),
                ('trainner', models.PositiveSmallIntegerField()),
                ('start_time', models.TimeField()),
                ('day_of_the_week', models.DateField()),
                ('end_time', models.TimeField()),
                ('date', models.DateField()),
                ('breaks', models.PositiveSmallIntegerField()),
            ],
        ),
    ]