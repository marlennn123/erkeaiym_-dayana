from .serializers import *
from .models import *
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .filter import *
from rest_framework.filters import SearchFilter


class FacultyViewSets(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = FacultyFilter
    search_fields = ['faculty_name']
    permission_classes = [permissions.IsAuthenticated]


class ProfessorViewSets(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProfessorFilter
    search_fields = ['professor_name']


class StudentViewSets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = StudentFilter
    search_fields = ['student_name', 'department']


class CourseViewSets(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = CourseFilter
    search_fields = ['course_name']

