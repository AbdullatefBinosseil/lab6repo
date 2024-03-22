from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

# Create your views here.
class studentForm(forms.Form):
    firstName= forms.CharField(label="First name")
    lastName= forms.CharField(label="Last name")
    age= forms.CharField(label="Age")
    phoneNum= forms.CharField(label="Phone number")
    #courses= forms.CharField(label="First name")
def students(request):
    students_list = student.objects.all()
    form = studentForm()
    if request.method == 'POST':
        form = studentForm(request.POST)
        #selecting the course
        if form.is_valid():
            
            form.save()
            return HttpResponseRedirect(reverse("app:students"))
    return render(request, 'students.html', {'students': students_list, 'form': form})

