from django.db import models
from django.core.validators import RegexValidator
from shared.django.model import BaseModel
from branch.models import Branch
from users.models import User

phone_regex = RegexValidator(
    regex=r'^998[0-9]{9}$',
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)


class ContactManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user__is_active=True)


class Contact(BaseModel):

    WORKING = 'Working'
    NOT_WORKING = 'Not Working'

    STATUS_CHOICES = (
        (WORKING, "Working"),
        (NOT_WORKING, "Not Working"),
    )

    MALE = "male"
    FEMALE = "female"

    GENDER_CHOICES = (
        (MALE, "male"),
        (FEMALE, "female"),
    )

    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)

    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, default=MALE)

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='contact', null=True, blank=True)
    phones = models.CharField(max_length=12, validators=[
        phone_regex], null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT, related_name='contacts', null=True,
                               blank=True)

    objects = ContactManager()

    @property
    def get_user(self):
        return self.user.id

    @property
    def full_name(self):
        fullname = ""
        if self.last_name:
            fullname += self.last_name
        if self.first_name:
            fullname += f" {self.first_name}"
        if self.middle_name:
            fullname += f" {self.middle_name}"
        return fullname

    @property
    def get_photo_url(self):
        if self.photo:
            return self.photo.url
        return None

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ('-id',)
