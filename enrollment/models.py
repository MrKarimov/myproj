from django.db import models
from common.models import BaseModel
# Create your models here.
class Enrollment(BaseModel):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='enrollments')
    student = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='enrollments')
    def __str__(self):
        return f'{self.course} - {self.student}'
