from django.db import models


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=16)
    description = models.TextField()

    def __str__(self):
        return self.faculty_name


class Professor(models.Model):
    professor_name = models.CharField(max_length=16)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.professor_name


class Student(models.Model):
    student_name = models.CharField(max_length=16)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    graduation_date = models.DateField(blank=True)

    def __str__(self):
        return self.student_name


class Cours(models.Model):
    cours_name = models.CharField(max_length=16)
    code = models.IntegerField()
    description = models.TextField()
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.cours_name