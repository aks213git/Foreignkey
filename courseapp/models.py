from django.db import models

class Course(models.Model):
    Course=models.CharField(max_length=255, null=True)
    Fee=models.IntegerField(null=True)

class Student(models.Model):
    name = models.CharField(max_length=255,null=True)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=255,null=True)
    join_date = models.DateField(null=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE,null=True)
    
