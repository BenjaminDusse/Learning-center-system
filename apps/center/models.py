from django.db import models
from shared.django.model import BaseModel

class Center(BaseModel):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

