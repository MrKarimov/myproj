from django.shortcuts import render
from django.views import View
from .models import Course

class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, "courses/course_list.html", {"courses": courses})
