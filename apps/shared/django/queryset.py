from django.db import models
from django.db.models import QuerySet


class BaseQuerySet(models.QuerySet):

    def delete(self):
        self.update(draft=True)


class DeleteManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return BaseQuerySet(self.model).filter(draft=False)
