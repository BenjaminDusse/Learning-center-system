from django.db import models
from shared.django.model import BaseModel

class Branch(BaseModel):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name