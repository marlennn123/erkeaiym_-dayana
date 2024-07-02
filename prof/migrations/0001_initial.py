# Generated by Django 5.0.6 on 2024-07-02 04:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=16)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor_name', models.CharField(max_length=16)),
                ('title', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prof.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cours_name', models.CharField(max_length=16)),
                ('code', models.IntegerField()),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField(default=0)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prof.faculty')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prof.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=16)),
                ('enrollment_date', models.DateField()),
                ('graduation_date', models.DateField(blank=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prof.faculty')),
            ],
        ),
    ]