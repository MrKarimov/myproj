
from django.urls import path
from .views import LessonListView
urlpatterns = [
    path('courses/',LessonListView.as_view(),name='lessons'),
]