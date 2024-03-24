from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from .models import student,course

# Create your views here.
class studentForm(forms.ModelForm):
    class Meta:
     model=student
     fields=["firstName", "lastName", "age", "phoneNum","courses"]
class courseForm(forms.ModelForm):
    class Meta:
     model=course
     fields="__all__"
def students(request):
     #course_list = course.objects.all()
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
     course_list = course.objects.all()
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
"form":courseForm(), "courses":course_list
})
def details(request,student_id):
   
    student_instance = student.objects.get(id=student_id)
    not_registered_courses = course.objects.exclude(students=student_instance)
    if request.method == 'POST':
        
        course_id = request.POST.get('course')
        selected_course = course.objects.get(id=course_id)
        student_instance.courses.add(selected_course)
        return HttpResponseRedirect(reverse('details', args=[student_id]))
    return render(request, 'app/details.html', {'student': student_instance, 'notRegisteredCourses': not_registered_courses})


