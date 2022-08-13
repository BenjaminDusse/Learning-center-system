from django.db import models
from shared.django.model import BaseModel
from branch.models import Branch

class Center(BaseModel):
    name = models.CharField(max_length=200)
    branch = models.OneToOneField(
        Branch, on_delete=models.PROTECT, related_name='center')

    def __str__(self):
        return self.name
