# Generated by Django 5.0.6 on 2024-07-04 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0002_rename_cours_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='faculty_name_en',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='faculty_name_ky',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='faculty_name_ru',
            field=models.CharField(max_length=16, null=True),
        ),
    ]