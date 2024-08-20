from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from classes.models import Classes
from courses.models import Courses
from classPeriod.models import ClassPeriod
from datetime import datetime

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Teacher
        fields="__all__"
class MinimalTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'classroom','Teacher_Name']

class  ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classes
        fields="__all__"
class MinimalClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['id', 'class_name','Capacity']
 
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields="__all__"
class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'course_name','course_Instructors']

class  ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassPeriod
        fields="__all__"
class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = ['id', 'course','start_Time']

class MinimalStudentSerializer(serializers.ModelSerializer):
    first_name=serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    def get_full_name(self, object):
         return f"{object.first_name} {object.last_name}"
    def get_age(self,object):
         today = datetime.now()
         age = today-object.date_of_birth
         return age


           