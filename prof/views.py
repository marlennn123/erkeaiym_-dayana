from .serializers import *
from .models import *
from rest_framework import viewsets


class FacultyViewSets(viewsets.ModelViewSet):
    queryset = Faculty.object.all()
    serializer_class = FacultySerializers

class ProfessorViewSets(viewsets.ModelViewSet):
    queryset = Professor.object.all()
    serializer_class = ProfessorSerializers

class StudentViewSets(viewsets.ModelViewSet):
    queryset = Student.object.all()
    serializer_class = StudentSerializers

class CoursViewSets(viewsets.ModelViewSet):
    queryset = Cours.object.all()
    serializer_class = CoursSerializers