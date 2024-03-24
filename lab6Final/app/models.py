from django.db import models


# Create your models here.


class course(models.Model):
    courseName= models.CharField(max_length=7)
    hour=models.IntegerField()
    def __str__(self):
        return f"{self.courseName}"

class student(models.Model):
    firstName= models.CharField(max_length=64)
    lastName= models.CharField(max_length=64)
    age= models.IntegerField()
    phoneNum= models.IntegerField()
    courses= models.ManyToManyField(course, related_name= "students")
    def __str__(self):
        return f"{self.firstName} {self.lastName} {self.age} {self.phoneNum}"




