import random
from statistics import mode
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from shared.django import model
from shared.django.model import BaseModel, DeleteModel
from users.validators import validate_file_extension
from course.models import Course


phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")


def random_number():
    return str(random.randint(1000000, 9999999))


class User(AbstractUser):
    photo = models.FileField(
        upload_to="user_documents/%Y/%m/%d", validators=[validate_file_extension])
    DARK = 'dark'
    LIGHT = 'light'
    THEMES_CHOICES = (
        (DARK, 'Dark'),
        (LIGHT, 'Light'),
    )
    UZ = 'uz'
    EN = 'en'
    RU = 'ru'

    LANGUAGES_CHOICES = (
        ('uz', 'Uzbek'),
        ('en', 'English'),
        ('ru', 'Russian'),
    )

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    ROLE_CHOICES = (
        ("admin", "admin"),
        ("student", "student"),
        ("teacher", "teacher"),
        ("staff", "staff"),
    )

    language = models.CharField(
        max_length=2, choices=LANGUAGES_CHOICES, default=UZ)
    theme = models.CharField(
        max_length=5, choices=THEMES_CHOICES, default=LIGHT)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    group = models.ForeignKey(
        'UserGroup', on_delete=models.CASCADE, related_name='user_group', blank=True, null=True)
    saldo = models.IntegerField(
        help_text='loan and salary', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name} Username: {self.username}'

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.fullname


class UserGroup(BaseModel):
    name = models.CharField(max_length=200)
    capacity = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='group')

    def __str__(self):
        return self.name


