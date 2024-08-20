from rest_framework import serializers
from student.models import Student
from classduration.models import ClassDuration
from teacher.models import Teacher
from course.models import Course
from lovelace.models import Lovelace

class MinimalStudentSerializer(serializers.ModelSerializer):
    class Meta:
      model = Student
      fields = ["id","first_name","email"]

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"

class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields = ["id","name"]

class StudentSerializer(serializers.ModelSerializer):
    course= CourseSerializer(many=True)
    class Meta:
        model = Student
        fields = "__all__"

class MinimalTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields = ["name","course"]

class TeacherSerializer(serializers.ModelSerializer):
    teacher_course=CourseSerializer(many=True)
    class Meta:
        model = Teacher
        fields = "__ all __"

class MinimalClassDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDuration
        fields = ["trainner","date"]

class ClassDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDuration
        fields = "__all__"

class MinimalLovelaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lovelace
        fields= ["capacity","hours"]

class LovelaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lovelace
        fields = "__all__"

