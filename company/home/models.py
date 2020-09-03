from django.db import models

# Create your models here.

class employee(models.Model):
    emp_fname=models.CharField(max_length=10)
    emp_lname=models.CharField(max_length=10)
    emp_mob=models.CharField(max_length=10,unique=True)
    emp_dept=models.ManyToManyField('department',related_name='dep_emp',blank=True)

    def __str__(self):
        return f"Employee:{self.emp_fname}  {self.emp_lname}"


class department(models.Model):
    dept_name=models.CharField(max_length=10)

    def __str__(self):
        return f"Department:{self.dept_name}"