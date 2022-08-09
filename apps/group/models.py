from django.db import models

from shared.django.model import BaseModel
from course.models import Course


class Group(BaseModel):
    name = models.CharField(max_length=200)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)


    def __str__(self):
        return self.name