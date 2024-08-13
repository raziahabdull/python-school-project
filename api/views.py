from django.shortcuts import render

# Create your views here.

from rest_framework.views import  APIView
from student.models import Student
from .serializers import StudentSerializer
from classduration.models import ClassDuration
from .serializers import  ClassDurationSerializer
from lovelace.models import Lovelace
from .serializers import LovelaceSerializer
from course.models import Course
from .serializers import CourseSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from rest_framework.response import Response
from rest_framework import status


class StudentListView(APIView):
    def get(self,request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            students = students.filter(first_name = first_name)
        if country:
            students = students.filter(country=country)
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer = StudentSerializer( data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    def get(self,request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(Student)
        return Response(serializer.data)

    def put(self,request,id):
        Student = student.objects.get(id=id)
        serializer = StudentSerializer(student,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors,status.HTTP_400_BAD_REQUEST)

        def delete(self,request,id):
            student = Student.objects.get(id=id)
            student.delete()
            return Response(status=status.HTTP_202_ACCEPTED)

        def enroll_student(self,student,course_id):
            course= Course.objects.get(id_course_id)
            student.courses.add(course)

        def post(self,request,id):
            student = Student.objects.get(id=id)
            action = request.data.get("action")
            if action =="enroll":
             course_id = request.data.get("course")
            self.enroll_student(student,course_id)
            return Response(status.HTTP_201_ACCEPTED)
class ClassDurationListView(APIView):
    def get(self,request):
        classduration = ClassDuration                                                                                                                                                                               .objects.all()
        serializer = ClassDurationSerializer(classduration,many=True)
        return Response(serializer.data)
   
    def post(self,request):
        serializer = ClassDurationSerializer(classduration,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class ClassDurationDetailView(APIView):
    def get(self,request,id):
        classduration = ClassDuration.objects.get(id=id)
        serializer = ClassDurationSerializer(ClassDuration)
        return Response(serializer.data)

    def put(self,request,id):
        classduration = ClassDuration.objects.get(id=id)
        serializer = ClassDurationSerializer(classduration,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors,status.HTTP_400_BAD_REQUEST)

        def delete(self,request,id):
            classduration = ClassDuration.objects.get(id=id)
            classduration.delete()
            return Response(status=status.HTTP_202_ACCEPTED)


class LovelaceListView(APIView):
    def get(self,request):
        lovelace = Lovelace.objects.all()
        serializer = LovelaceSerializer(lovelace,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = LovelaceSerializer( data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class LovelaceDetailView(APIView):
    def get(self,request,id):
        lovelace = Lovelace.objects.get(id=id)
        serializer = LovelaceSerializer(Lovelace)
        return Response(serializer.data)

    def put(self,request,id):
        lovelace = Lovelace.objects.get(id=id)
        serializer = LovelaceSerializer(lovelace,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors,status.HTTP_400_BAD_REQUEST)

        def delete(self,request,id):
            lovelace = Lovelace.objects.get(id=id)
            Lovelace.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
             def enroll_student(self,student,lovelace_id):
            lovelace= Lovelace.objects.get(id_lovelace_id)
            student.lovelace.add(lovelace)

        def post(self,request,id):
            student = Student.objects.get(id=id)
            action = request.data.get("action")
            if action =="enroll":
             lovelace_id = request.data.get("lovelace")
            self.enroll_student(student,lovelace_id)
            return Response(status.HTTP_201_ACCEPTED)


         def delete(self,request,id):
            teacher = Teacher.objects.get(id=id)
            teacher.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
            def assign_class(self,student,lovelace_id):
            lovelace= Lovelace.objects.get(id_course_id)
            teacher.lovelace.add(lovelace)

        def post(self,request,id):
            student = Student.objects.get(id=id)
            action = request.data.get("action")
            if action =="assigned_class":
             course_id = request.data.get("class")
            self.assign_class(student,lovelace_id)
            return Response(status.HTTP_201_ACCEPTED)
    

class CourseListView(APIView):
    def get(self,request):
        course = Course.objects.all()
        serializer = CourseSerializer(Course,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CourseSerializer( data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
class CourseDetailView(APIView):
    def get(self,request,id):
        course= Course.objects.get(id=id)
        serializer = CourseSerializer(Course)
        return Response(serializer.data)

    def put(self,request,id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(lovelace,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors,status.HTTP_400_BAD_REQUEST)

        def delete(self,request,id):
            course = Course.objects.get(id=id)
            Course.delete()
            return Response(status=status.HTTP_202_ACCEPTED)



class TeacherListView(APIView):
    def get(self,request):
        Teacher = Teacher.objects.all()
        serializer = TeacherSerializer(Teacher,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TeacherSerializer( data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def get(self,request,id):
        teacher= Teacher.objects.get(id=id)
        serializer = TeacherSerializer(Course)
        return Response(serializer.data)

    def put(self,request,id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(lovelace,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors,status.HTTP_400_BAD_REQUEST)

        def delete(self,request,id):
            teacher = Teacher.objects.get(id=id)
            teacher.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
            def assign_course(self,student,course_id):
            course= Course.objects.get(id_course_id)
            teacher.courses.add(course)

        def post(self,request,id):
            student = Student.objects.get(id=id)
            action = request.data.get("action")
            if action =="assigned_course":
             course_id = request.data.get("course")
            self.assign_course(student,course_id)
            return Response(status.HTTP_201_ACCEPTED)
    
