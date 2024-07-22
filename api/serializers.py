from rest_framework import serializers
from student.models import Student
from classduration.models import ClassDuration
from teacher.models import Teacher
from course.models import Course
from lovelace.models import Lovelace

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__ all __"
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
        
class ClassDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDuration
        fields = "__all__"

class LovelaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lovelace
        fields = "__all__"