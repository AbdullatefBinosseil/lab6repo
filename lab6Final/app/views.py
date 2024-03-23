from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from .models import student,course

# Create your views here.
class studentForm(forms.ModelForm):
    class Meta:
     model=student
     fields=["firstName", "lastName", "age", "phoneNum"]
class courseForm(forms.ModelForm):
    class Meta:
     model=course
     fields="__all__"
def students(request):
     students_list = student.objects.all()
     if request.method == "POST":      
        form=studentForm(request.POST)
        
        if(form.is_valid):
            form.save()
            return HttpResponseRedirect(reverse("students"))
        else:
          return render(request, "app/student.html", {
            "message": "Invalid data entered for a student"
         })


     else:
        return render(request, "app/student.html", {
"form":studentForm(),"students":students_list
})
def courses(request):
     if request.method == "POST":      
        form=courseForm(request.POST)
        
        if(form.is_valid):
            form.save()
            return HttpResponseRedirect(reverse("courses"))
        else:
          return render(request, "course.html", {
            "message": "Invalid data entered for a course."
         })

     else:
        return render(request, "app/course.html", {
"form":courseForm()
})


