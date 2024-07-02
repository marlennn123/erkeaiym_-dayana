from rest_framework import serializers
from .models import *

class FacultySerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class  ProfessorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class  StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class  CoursSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = '__all__'



