from django.shortcuts import render
from .models import Lesson
from django.views import View

# Create your views here.
class LessonListView(View):
    def get(self,request):
        lessons = Lesson.objects.all()
        return render(request,'lessons/lessons.html',{'lessons':lessons})
    
class LessonDetailView(View):
    def get(self,request,pk):
        lesson = Lesson.objects.get(pk=pk)
        return render(request,'lessons/lesson_detail.html',{'lesson':lesson})
    