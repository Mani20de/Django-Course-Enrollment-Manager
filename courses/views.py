from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse 
# Create your views here.
from .models import Course, Enrollment, StudentProfile
from django.contrib.auth.decorators import login_required 
def index(request):
    return render (request, "courses/index.html")

def courses(request):
    courses = Course.objects.all()
    return render(request, "courses/courses.html", {
        "courses": courses,
    })

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    enrollment_count = Enrollment.objects.filter(course=course).count()


    return render(request, "courses/course_detail.html", {
        "course": course,
        "enrollment_count": enrollment_count
    })

@login_required
def enroll(request, course_id):
    if request.method != "POST":
        return redirect("course_detail", course_id=course_id)
    course = get_object_or_404(Course, id=course_id)
    student = StudentProfile.objects.get(user=request.user)

    already_enrolled = Enrollment.objects.filter(
        student = student,
        course = course,
    ).exists()
    if already_enrolled:
        return redirect("course_detail", course_id=course.id)
    current_enrollment = Enrollment.objects.filter(course=course).count()
    if current_enrollment >= course.capacity:
        return redirect("course_detail", course_id=course.id)
    Enrollment.objects.create(
        student = student,
        course = course,
        status = "enrolled"
    )
    return redirect("course_detail", course_id=course.id)

