from django.contrib import admin
from .models import Student, Marks, Hostel

# Customize the Student admin view
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # Columns to show side-by-side
    list_display = ('regno', 'name', 'class_name', 'branch', 'year')
    # Fields searchable via the top search bar
    search_fields = ('regno', 'name', 'branch')
    # Sort by registration number automatically
    ordering = ('regno',)


# Customize the Marks admin view
@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    # Columns to show side-by-side
    list_display = ('regno', 'exam_type', 'subject', 'marks', 'grade')
    # Fields searchable via the top search bar
    search_fields = ('regno__regno', 'regno__name', 'subject', 'exam_type')
    # Filter tools on the right-hand panel
    list_filter = ('exam_type', 'grade')


# Customize the Hostel admin view
@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    # Columns to show side-by-side
    list_display = ('regno', 'hostel_name', 'room_no')
    # Fields searchable via the top search bar
    search_fields = ('regno__regno', 'regno__name', 'hostel_name', 'room_no')
    # Filter tools on the right-hand panel
    list_filter = ('hostel_name',)
