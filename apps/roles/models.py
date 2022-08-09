import random
from django.db import models
from shared.django.model import BaseModel

from users.models import User
from center.models import Center
from group.models import Group


STUDYING = 'Studying'
NOT_STUDYING = 'Not Studying'


def random_number():
    return str(random.randint(1000000, 9999999))


STATUS_CHOICES = (
    ('Studying', STUDYING),
    ("Not Studying", NOT_STUDYING)
)


class Student(BaseModel):
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='student_group')
    student_number = models.CharField(max_length=7, unique=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=STUDYING)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='students')
    learning_center = models.ForeignKey(
        Center, on_delete=models.SET_NULL, null=True, blank=True)

# datetime.strftime("%-d %B %Y, %I:%M:%S%p")

    def __str__(self) -> str:
        return self.user.fullname

    def save(self, *args, **kwargs):
        self.student_number = random_number()
        super(Student, self).save(*args, **kwargs)


WORKING = "Working"
NOT_WORKING = "Not Working"

STATUS_CHOICES = (
    (WORKING, "Working"),
    (NOT_WORKING, "Not Working"),
)


class Teacher(BaseModel):
    teacher_number = models.CharField(max_length=7)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=WORKING)
    saldo = models.DecimalField(
        help_text='load and salary', max_digits=9, decimal_places=3)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='teacher_user')
    learning_center = models.OneToOneField(
        Center, on_delete=models.CASCADE, related_name='teacher_center')

    def save(self, *args, **kwargs):
        self.student_number = random_number()
        super(Teacher, self).save(*args, **kwargs)
