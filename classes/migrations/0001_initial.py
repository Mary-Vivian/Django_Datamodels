# Generated by Django 5.0.6 on 2024-06-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('class_id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('room_number', models.CharField(max_length=20)),
                ('teacher_allocated', models.CharField(max_length=20)),
                ('course_tought', models.CharField(max_length=20)),
                ('course_start_time', models.TimeField()),
                ('course_end_time', models.TimeField()),
                ('course_day_of_week', models.CharField(max_length=20)),
                ('seating_arrangement', models.TextField()),
                ('equipment', models.TextField()),
            ],
        ),
    ]
