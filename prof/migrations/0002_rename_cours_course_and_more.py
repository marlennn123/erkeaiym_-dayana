# Generated by Django 5.0.6 on 2024-07-02 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cours',
            new_name='Course',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='cours_name',
            new_name='course_name',
        ),
    ]
