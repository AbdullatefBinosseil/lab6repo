from django.db import models


# Create your models here.


class course(models.Model):
    courseName= models.CharField(max_length=7)
    hour=models.IntegerField(default=3)
    def __str__(self):
        return f"{self.courseName} {self.hour}"

class student(models.Model):
    firstName= models.CharField(max_length=64)
    lastName= models.CharField(max_length=64)
    age= models.IntegerField(null=True)
    phoneNum= models.IntegerField(null=True)
    courses= models.ManyToManyField(course, related_name= "students")
    def __str__(self):
        return f"{self.firstName} {self.lastName} {self.age} {self.phoneNum} {self.courses}"




