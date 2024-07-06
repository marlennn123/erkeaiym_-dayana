from django_filters.rest_framework import FilterSet
from .models import *


class FacultyFilter(FilterSet):
    class Meta:
        model = Faculty
        fields = {
        'faculty_name': ['exact'],

        }


class ProfessorFilter(FilterSet):
    class Meta:
        model = Professor
        fields = {
        'professor_name': ['exact'],

        }


class StudentFilter(FilterSet):
    class Meta:
        model = Student
        fields = {
        'student_name': ['exact'],

        }


class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
        'price': ['gt', 'lt'],

        }