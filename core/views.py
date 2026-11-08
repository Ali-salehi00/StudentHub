from django.shortcuts import render, redirect
from .models import Student


def student_list(request):

    if request.method == 'POST':
        Student.objects.create(
            fname=request.POST.get('fname'),
            lname=request.POST.get('lname'),
            student_number=request.POST.get('student_number'),
            major=request.POST.get('major')
        )

        return redirect('student_list')

    students = Student.objects.all()

    return render(request, 'students.html', {
        'students': students
    })