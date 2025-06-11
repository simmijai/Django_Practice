

# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from core.utils.logger import logger
from django.contrib.auth.decorators import login_required
import logging
logger = logging.getLogger(__name__)




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

# # Add a student
# def add_student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#     else:
#         form = StudentForm()
#     return render(request, 'core/add_student.html', {'form': form})

# # Edit a student
# def edit_student(request, pk):
#     student = get_object_or_404(Student, pk=pk)

#     if request.method == 'POST':
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#     else:
#         form = StudentForm(instance=student)

#     return render(request, 'core/add_student.html', {'form': form})



# def manage_student(request, pk=None):
#     if pk:
#         student = get_object_or_404(Student, pk=pk)
#     else:
#         student = None

#     form = StudentForm(request.POST or None, instance=student)

#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             if pk:
#                 messages.success(request, 'Student updated successfully!')
#             else:
#                 messages.success(request, 'Student added successfully!')
#             return redirect('student_list')
#         else:
#             print("❌ Form Errors:", form.errors)

#     return render(request, 'core/add_student.html', {'form': form})



def manage_student(request, pk=None):
    if pk:
        logger.debug(f"Edit Mode: Fetching student with id={pk}")
        student = get_object_or_404(Student, pk=pk)
    else:
        logger.debug("Add Mode: Creating new student")
        student = None

    form = StudentForm(request.POST or None, instance=student)

    if request.method == 'POST':
        if form.is_valid():
            saved_student = form.save()
            if pk:
                logger.info(f"Updated student: {saved_student}")
                messages.success(request, 'Student updated successfully!')
            else:
                logger.info(f"Created new student: {saved_student}")
                messages.success(request, 'Student added successfully!')
            return redirect('student_list')
        else:
            logger.warning(f"Form submission failed. Errors: {form.errors}")

    return render(request, 'core/add_student.html', {'form': form})



# Delete a student
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'core/confirm_delete.html', {'student': student})

@login_required
def dashboard_view(request):
    logger.info(f"User {request.user.username} accessed dashboard.")
    return render(request, 'core/dashboard.html')