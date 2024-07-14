from rest-framework import serializer
from student.models import Student

class StudentSerializer(serializers.Modelserializer):
    class Meta:
        model = Student
        fields = "_ _all_ _"

class TeacherSerializer(serializers.Modelserializer):
    class Meta:
        model = Teacher
        fields = "_ _ all _ _"
class CourseSerializer(serializer.Modelserializer):
    class Meta:
        model = Course
        fields = "_ _all_ _"
        
class ClassDurationSerializer(serializer.Modelserializer):
    class Meta:
        model = Course
        fields = "_ _all_ _"