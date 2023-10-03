from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add, name="add"),
    path('stud/', views.stud, name="stud"),
    path('coursedb/', views.coursedb, name="coursedb"),
    path('show_student/', views.show_student, name='show_student'),
    path('add_student/', views.add_student, name='add_student'), 
     path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete/<int:pk>/', views.delete, name='delete'),

]
