# Generated by Django 4.1 on 2022-09-01 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_place_of_residence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_class',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
