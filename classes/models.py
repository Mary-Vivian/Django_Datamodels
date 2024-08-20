from django.db import models
from teacher.models import Teacher
from courses.models import Courses

class Classes(models.Model):
    id = models.AutoField(primary_key=True)  
    class_name = models.CharField(max_length=20, default='Default Class Name')
    number_of_seats = models.IntegerField(default=0)  
    number_of_students = models.IntegerField(default=0)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='classes')
    courses = models.ManyToManyField(Courses, related_name='classes')  
    available_equipments = models.TextField()
    description = models.TextField(default='No description available')

    def __str__(self):
        return f"{self.class_name} {self.class_teacher}"
