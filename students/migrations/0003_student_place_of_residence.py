# Generated by Django 4.1 on 2022-08-31 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_remove_student_course_remove_student_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='place_of_residence',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
