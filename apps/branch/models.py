from django.db import models
from shared.django.model import BaseModel
from center.models import Center


class Branch(BaseModel):
    name = models.CharField(max_length=50)
    center = models.OneToOneField(
        Center, on_delete=models.PROTECT, related_name='branch_center')

    def __str__(self):
        return self.name
