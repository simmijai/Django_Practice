from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'gender', 'phone', 'date_of_birth']
    search_fields = ['name', 'email']
