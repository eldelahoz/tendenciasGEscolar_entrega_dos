# Generated by Django 4.2.15 on 2024-11-02 07:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('start_time', models.TimeField(default=datetime.time(0, 0))),
                ('end_time', models.TimeField(default=datetime.time(0, 0))),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher')),
            ],
        ),
    ]
