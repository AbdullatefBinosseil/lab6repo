from django.db import models

# Create your models here.
class student(models.Model):
    firstName= models.CharField(max_length=64)
    lastName= models.CharField(max_length=64)
    age= models.IntegerField
    phoneNum= models.IntegerField
    courses= models.ManyToManyField(course, blank= True, related_name= "students")
    def __str__(self):
        return f"{self.firstName} {self.lastName} {self.age} {self.phoneNum} {self.courses}"

class course(models.Model):
    courseName= models.CharField(max_length=7)


