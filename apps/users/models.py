import random
from statistics import mode
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from shared.django.model import BaseModel, DeleteModel
from users.validators import validate_file_extension


phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")


def random_number():
    return str(random.randint(1000000, 9999999))


WORKING = 'Working'
NOT_WORKING = 'Not Working'

STATUS_CHOICES = (
    (WORKING, "Working"),
    (NOT_WORKING, "Not Working"),
)


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
    roles = models.ManyToManyField('users.Role', blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(
        validators=[phone_regex], max_length=12, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField(blank=True, null=True)
    language = models.CharField(
        max_length=25, choices=LANGUAGES_CHOICES, blank=True, null=True, default=EN)
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


class Role(BaseModel, DeleteModel):
    ROLE_CHOICES = (
        ("admin", "admin"),
        ("student", "student"),
        ("teacher", "teacher"),
        ("staff", "staff"),
    )

    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_roles')
    groups = models.ManyToManyField('auth.Group')
    unique_name = models.CharField(max_length=255, choices=ROLE_CHOICES)
    saldo = models.IntegerField(
        help_text='loan and salary', null=True, blank=True)

    class Meta:
        ordering = ('-modified_date', )

    def __str__(self):
        return f"{self.title}"


class UserActivity(models.Model):
    # Login Status
    LOGGED_IN = 'LOGGED_IN'
    LOGGED_OUT = 'LOGGED_OUT'
    LOGIN_FAILED = 'LOGIN_FAILED'

    ACTION = (
        (LOGGED_IN, 'LOGGED_IN'),
        (LOGGED_OUT, 'LOGGED_OUT'),
        (LOGIN_FAILED, 'LOGIN_FAILED')
    )

    ip = models.GenericIPAddressField(null=True, blank=True)
    login_datetime = models.DateTimeField(auto_now=True)
    action = models.CharField(max_length=12, default=LOGGED_IN, choices=ACTION)
    user_agent_info = models.CharField(max_length=255, null=True, blank=True)

    user = models.ForeignKey('users.User', on_delete=models.SET_NULL,
                             related_name='users_login', null=True, blank=True)

    def __str__(self):
        return self.user.contact.full_name

    class Meta:
        ordering = ('-id',)
