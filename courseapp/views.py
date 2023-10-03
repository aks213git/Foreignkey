from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Course, Student

def home(request):
    return render(request, 'home.html')

def add(request):
    return render(request, 'add_course.html')

def stud(request):
    courses = Course.objects.all()
    return render(request, 'add_student.html', {'courses': courses})

def coursedb(request):
    if request.method == "POST":
        course_name = request.POST.get('course')
        course_fee = request.POST.get('fee')
        course = Course(Course=course_name, Fee=course_fee)
        course.save()
        return redirect('coursedb')   
    return render(request, 'add_course.html')

def show_student(request):
    students = Student.objects.select_related('course').all()
    return render(request, 'show_student.html', {'students': students})

def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        age = request.POST.get('age')
        join_date = request.POST.get('join_date')
        course_id = request.POST.get('course')
        
        course = Course.objects.get(id=course_id)
        
        student = Student(name=name, address=address, age=age, join_date=join_date, course=course)
        student.save()
        
        return redirect('show_student')

    courses = Course.objects.all()
    return render(request, 'add_student.html', {'courses': courses})

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        age = request.POST.get('age')
        join_date = request.POST.get('join_date')
        course_id = request.POST.get('course')
        
        course = Course.objects.get(id=course_id)
        
        student.name = name
        student.address = address
        student.age = age
        student.join_date = join_date
        student.course = course
        student.save()
        
        return redirect('show_student')

    courses = Course.objects.all()
    return render(request, 'edit_student.html', {'student': student, 'courses': courses})

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        age = request.POST.get('age')
        join_date = request.POST.get('join_date')
        course_id = request.POST.get('course')
        
        course = Course.objects.get(id=course_id)
        
        student.name = name
        student.address = address
        student.age = age
        student.join_date = join_date
        student.course = course
        student.save()
        
        return redirect('show_student')

    courses = Course.objects.all()
    return render(request, 'edit_student.html', {'student': student, 'courses': courses})


def delete(request,pk):
    e=Student.objects.get(id=pk)
    e.delete()
    return redirect('show_student')


