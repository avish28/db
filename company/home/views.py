from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,"home/home.html")

def dept(request):
    return render(request,"home/department.html")
