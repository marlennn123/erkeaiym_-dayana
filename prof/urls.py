from django.urls import path
from .views import FacultyViewSets, ProfessorViewSets, StudentViewSets, CourseViewSets


urlpatterns = [
    path('', FacultyViewSets.as_view({'get': 'list', 'post': 'create'}), name = 'faculty_list'),
    path('<int:pk>/', FacultyViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                               'delete': 'destroy'}), name = 'faculty_detail'),

    path('professor/', ProfessorViewSets.as_view({'get': 'list', 'post': 'create'}), name='professor_list'),
    path('professor/<int:pk>/', ProfessorViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                               'delete': 'destroy'}), name='professor_detail'),

    path('student/', StudentViewSets.as_view({'get': 'list', 'post': 'create'}), name='student_list'),
    path('student/<int:pk>/', StudentViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                               'delete': 'destroy'}), name='student_detail'),

    path('course/', CourseViewSets.as_view({'get': 'list', 'post': 'create'}), name='course_list'),
    path('course/<int:pk>/', CourseViewSets.as_view({'get': 'retrieve', 'put': 'update',
                                               'delete': 'destroy'}), name='course_detail'),
]