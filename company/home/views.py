from django.shortcuts import render
from .models import department,employee

# Create your views here.

def homepage(request):
    return render(request,"home/home.html")

def dept(request):
    d1=department.objects.all()

    return render(request,"home/department.html",
                  {'department':d1
                   })

def emp(request):
    e1=employee.objects.all()
    return  render(request,"home/employee.html",
                   {'employee':e1})

def depemp(request,dept_id):
    deinfo = department.objects.get(pk=dept_id);
    if request.method=="POST":
          e1=employee(emp_fname=request.POST["addf"],emp_lname=request.POST["addl"],emp_mob=request.POST["addm"])
          e1.save()
          e1.emp_dept.add(deinfo)

    einfo=deinfo.dep_emp.all()
    return  render(request,"home/depemp.html",
                   {'employee':einfo})





