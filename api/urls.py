from django.urls import path                        
from .views import StudentListView
from .views import CourseListView
from  .views import ClassDurationListView 
from .views import LovelaceListView 
from .views import StudentDetailView
from .views import TeacherListView
from .views import LovelaceDetailView
from .views import CourseDetailView
from .views import TeacherDetailView
from .views import ClassDurationDetailView

urlpatterns =[
    path("Student/",StudentListView.as_view(),name="student_list_view"),
    path("Teacher/",TeacherListView.as_view(),name="teacher_list_view"),
    path("Course/",CourseListView.as_view(),name="course_list_view"),
    path("ClassDuration/",ClassDurationListView.as_view(),name="classduration_list_view"),
    path("Lovelace/",LovelaceListView.as_view(),name="lovelace_list_view"),
    path("Student/<int:id>/",StudentDetailView.as_view(),name ="student_detail_view"),
    path("Teacher/<int:id>/",TeacherDetailView.as_view(),name="teacher_detail_view"),
    path("Course/<int:id>/",CourseDetailView.as_view(),name="course_detail_view"),
    path("ClassDuration/<int:id>/",ClassDurationDetailView.as_view(),name="classduration_detail_view"),
    path("Lovelace/<int:id>/",LovelaceDetailView.as_view(),name="lovelace_detail_view"),
]