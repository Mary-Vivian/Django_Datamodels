from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    code = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    courses=models.TextField()
    country = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

