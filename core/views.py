

# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def home(request):
    return HttpResponse('THis is my first function')

def home_view(request):
    context = {
        'name': 'Simmi',
        'title': 'Django Learning',
    }
    return render(request, 'home.html', context)


# List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})

# Add a student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'core/add_student.html', {'form': form})

# Edit a student
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'core/add_student.html', {'form': form})

# Delete a student
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'core/confirm_delete.html', {'student': student})
