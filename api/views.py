# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import Student
from classes.models import Classes
from courses.models import Courses
from teacher.models import Teacher
from classPeriod.models import ClassPeriod
from .serializers import StudentSerializer
from .serializers import CoursesSerializer
from .serializers import ClassesSerializer
from .serializers import TeacherSerializer
from .serializers import ClassPeriodSerializer
from rest_framework import status
from .serializers import MinimalStudentSerializer
from .serializers import MinimalClassesSerializer
from .serializers import MinimalClassPeriodSerializer
from .serializers import MinimalTeacherSerializer
from .serializers import MinimalCourseSerializer

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            students = students.filter(first_name=first_name)
        country = request.query_params.get("country")
        if country:
            students = students.filter(country=country)
        serializer = MinimalStudentSerializer(students, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class StudentDetailview(APIView):
     def put(self,request,id):
       student=Student.objects.get(id=id)
       serializer=StudentSerializer(student,data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     def enroll(self, student,course_code):
         course=Courses.objects.get(id=course_code)
         student.course.add(course)

   

     def post(self, request, id):
        student = Student.objects.get(id=id)
        action = request.data.get("action")
        if action == "enroll":
            course_code = request.data.get("course_code")
            self.enroll(student, course_code)
        serializer = MinimalStudentSerializer(student) 
        return Response(serializer.data, status=status.HTTP_200_OK)

     def delete(self,request,id):
       student=Student.objects.get(id=id)
       student.delete()
       return Response(status=status.HTTP_202_ACCEPTED)  
      
   
   
class CoursesListView(APIView):
    def get(self, request):
        courses = Courses.objects.all()
        serializer = MinimalCourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MinimalCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class CoursesDetailview(APIView):
    def put(self,request,id):
       courses=Courses.objects.get(id=id)
       serializer=StudentSerializer(courses,data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
       courses=Courses.objects.get(id=id)
       courses.delete()
       return Response(status=status.HTTP_202_ACCEPTED)           

class ClassesListView(APIView):
    def get(self, request):
        classes = Classes.objects.all()
        serializer = MinimalClassesSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MinimalClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ClassesDetailview(APIView):
    def put(self,request,id):
        classes= Classes.objects.get(id=id)
        serializer =ClassesSerializer(classes, data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
       classes=Classes.objects.get(id=id)
       classes.delete()
       return Response(status=status.HTTP_202_ACCEPTED)         

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = MinimalTeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MinimalTeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailview(APIView):
   def put(self,request,id):
        teacher= Teacher.objects.get(id=id)
        serializer =TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   def delete(self,request,id):
       teachers=Teacher.objects.get(id=id)
       teachers.delete()
       return Response(status=status.HTTP_202_ACCEPTED)  
                 
class ClassPeriodListView(APIView):
    def get(self, request):
        classPeriod = ClassPeriod.objects.all()
        serializer = MinimalClassPeriodSerializer(classPeriod, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MinimalClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassPeriodDetailview(APIView):
   def put(self,request,id):
        classPeriod= ClassPeriod.objects.get(id=id)
        serializer =TeacherSerializer(classPeriod,data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
   def delete(self,request,id):
       classPeriod=ClassPeriod.objects.get(id=id)
       classPeriod.delete()
       return Response(status=status.HTTP_202_ACCEPTED)
   
class AssignStudentToClass(APIView):
    def post(self, request, class_period_id):
        try:
            class_period = ClassPeriod.objects.get(id=class_period_id)
        except Class_Period.DoesNotExist:
            return Response({'error': 'Class period not found'}, status=status.HTTP_404_NOT_FOUND)
        student_id = request.data.get('student_id')
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        class_period.student = student
        class_period.save()
        serializer = ClassPeriodSerializer(class_period)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class AssignTeacherToClassroom(APIView):
    def post(self, request, classroom_id):
        try:
            classroom = Classes.objects.get(id=classroom_id)
        except Classes.DoesNotExist:
            return Response({'error': 'Classroom not found'}, status=status.HTTP_404_NOT_FOUND)
        teacher_id = request.data.get('teacher_id')
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return Response({'error': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)
        classroom.class_teacher = teacher
        classroom.save()
        serializer = ClassesSerializer(classroom)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class WeeklyTimetable(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
       

            

























