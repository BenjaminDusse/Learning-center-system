import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from users.validators import validate_file_extension


phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")


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
    OZ = 'oz'
    RU = 'ru'

    LANGUAGES_CHOICES = (
        ('uz', 'Lotin'),
        ('oz', 'Uzbek'),
        ('ru', 'Russian'),
    )

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    username = models.CharField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(
        validators=[phone_regex], max_length=12, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField(blank=True, null=True)
    language = models.CharField(
        max_length=25, choices=LANGUAGES_CHOICES, blank=True, null=True)
    theme = models.CharField(
        max_length=24, choices=THEMES_CHOICES, default=DARK, blank=True, null=True)
    date_of_birth = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.username

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
        # if self.date_of_birth:
        #     self.date_of_birth = self.date_of_birth.strftime("%-d %B %Y")
        super(User, self).save(*args, **kwargs)
