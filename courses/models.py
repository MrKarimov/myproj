from django.db import models
from common.models import BaseModel
# Create your models here.
class Course(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, related_name='courses')
    instructor = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='courses')
    students = models.ManyToManyField('accounts.CustomUser', related_name='courses_joined')
    def __str__(self):
        return self.title
    