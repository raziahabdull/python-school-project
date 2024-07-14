from django.urls import path
from .views import StudentListView

urlpatterns =[
    path("students/",StudentListView.as_view(),name="student_list_view"),
    
]
urlpatterns =[
    path("Teacher/",TeacherListView.as_view(),name="teacher_list_view"),
    
]
urlpatterns =[
    path("Course/",CourseListView.as_view(),name="course_list_view"),
    
]
urlpatterns =[
    path("ClassDuration/",ClassDurationListView.as_view(),name="classduration_list_view"),
    
]
urlpatterns =[
    path("Lovelace/",ClassDurationListView.as_view(),name="lovelace_list_view"),
    
]