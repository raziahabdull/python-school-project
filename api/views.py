from django.shortcuts import render

# Create your views here.
from rest-framework.views import  APIView
from student.models import Student
from classduration import ClassDuration
from lovelace import Lovelace
from  course import Course
from .serializers import StudentSerializer
from rest-framework import Response

class StudentListView(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)

class ClassDurationListView(APIView):
    def get(self,request):
        classduration = ClassDuration.objects.all()
        serializer = ClassDurationSerializer(students,many=True)
        return Response(serializer.data)

class LovelaceListView(APIView):
    def get(self,request):
        lovelace = Lovelace.objects.all()
        serializer = LovelaceSerializer(students,many=True)
        return Response(serializer.data)

class CourseListView(APIView):
    def get(self,request):
        course = Course.objects.all()
        serializer = CourseSerializer(students,many=True)
        return Response(serializer.data)