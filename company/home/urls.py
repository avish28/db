from . import views
from django.urls import path

urlpatterns=[

    path('',views.homepage,name='home'),
    path('department',views.dept,name='dept'),

]