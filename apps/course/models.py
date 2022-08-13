import imp
from django.db import models
from shared.django.model import BaseModel

from center.models import Center


class Course(BaseModel):
    center = models.ForeignKey(
        Center, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name
