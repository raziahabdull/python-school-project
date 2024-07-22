from django import urls
from django.urls import path                        
from .views import StudentListView, CourseListView, ClassDurationListView, LovelaceListView, StudentDetailView,TeacherListView

urlpatterns =[
    path("Students/",StudentListView.as_view(),name="student_list_view"),
    
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
    path("Lovelace/",LovelaceListView.as_view(),name="lovelace_list_view"),
    
]
urlpatterns =[
    path("Students/<int:id>/",StudentDetailView.as_view(),name ="student_detail_view"),
]