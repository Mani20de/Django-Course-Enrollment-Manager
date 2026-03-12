from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20)
    major = models.CharField(max_length=100)
    semester = models.IntegerField()
    def __str__(self):
        return f"{self.user.username} ({self.student_id})"
   

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    credits = models.IntegerField()
    def __str__(self):
        return f"{self.code} - {self.title}"


class Enrollment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ("enrolled", "Enrolled"),
        ("dropped", "Dropped"),
        ("completed", "Completed"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["student", "course"], name="unique_student_course")
        ]
    def __str__(self):
        return f"{self.student.user.username} in {self.course.code}"