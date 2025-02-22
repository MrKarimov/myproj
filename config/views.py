from  django.shortcuts import render
from courses.models import Course

def home_page(request):
    activ_course = Course.objects.filter()

    return render(request, 'home.html',context={'courses':activ_course})
