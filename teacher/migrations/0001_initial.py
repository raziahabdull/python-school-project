# Generated by Django 5.0.7 on 2024-07-22 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=15)),
                ('department', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('course', models.CharField(max_length=50)),
                ('teacher_id', models.PositiveSmallIntegerField()),
                ('bank_account_number', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=5)),
            ],
        ),
    ]
