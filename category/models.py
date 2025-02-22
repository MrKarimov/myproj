from django.db import models

from common.models import BaseModel


class Category(BaseModel):
     name = models.CharField(max_length=255, unique=True)
     description = models.TextField(blank=True, null=True)

     def __str__(self):
        return self.name
