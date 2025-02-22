from django.db import models

# Create your models here.
from common.models import BaseModel

class Lesson(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='lessons')
    video_url = models.URLField()
    order = models.PositiveIntegerField()
    def __str__(self):
        return self.title