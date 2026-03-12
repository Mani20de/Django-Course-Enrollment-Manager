from django.contrib import admin
from .models import StudentProfile, Instructor, Course, Enrollment
# Register your models here.

admin.site.register(StudentProfile)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Enrollment)

