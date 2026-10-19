from django.urls import path
from scool.views import *


urlpatterns = [
    path('', CourseListAPI.as_view()),
    path('course_details/<str:id>/', CoursedetailsAPI.as_view()),

    path('student_list/', SubjectListAPI.as_view()),
    path('student_details/<str:id>/', SubjectDetailsAPI.as_view()),
    path('student_all/<str:id>/', SubjectIndividual.as_view()),
]