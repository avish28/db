from . import views
from django.urls import path

urlpatterns=[

    path('',views.homepage,name='home'),
    path('department',views.dept,name='dept'),
    path('employee',views.emp,name='empl'),
    path('depemp/<int:dept_id>',views.depemp,name='de')

]