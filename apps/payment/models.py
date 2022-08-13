from secrets import choice
from django.db import models
from center.models import Center
from shared.django.model import BaseModel
from users.models import User, random_number
from branch.models import Branch


class Payment_type(BaseModel):
    monthly_bill = models.ForeignKey(
        'payment.Monthly_Bill', on_delete=models.PROTECT, related_name='payment_type')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Payment_history(BaseModel):
    CASH = 'Naqd'
    PLASTIC_CARD = 'Plastik kartochka'
    MONEY_TRANSFER = "Pul o'tkazish"

    PAYMENT_TYPE = (
        (CASH, "Cash"),
        (PLASTIC_CARD, "Plastic Card"),
        (MONEY_TRANSFER, "Money Transfer")
    )
    payment_number = models.CharField(max_length=7, unique=True, blank=True)
    payment_type = models.CharField(max_length=200, choices=PAYMENT_TYPE)
    # kalla kere maqsad kimgadur tolidi pulni shuni hal qilish kere
    price = models.FloatField()
    learning_center = models.ForeignKey(
        Center, on_delete=models.CASCADE, related_name="payment_history")
    user = models.ManyToManyField(
        User, related_name='history_user')
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE, related_name="history_branch")

    def __str__(self):
        return self.payment_number

    def save(self, *args, **kwargs):
        self.payment_number = random_number()
        super().save(*args, **kwargs)


class Loan(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='loan_user')
    price = models.FloatField()

    def __str__(self):
        return f"{self.user.fullname}'s loans"


class Monthly_Bill(BaseModel):
    name = models.CharField(max_length=200)
    fixed_percentage = models.IntegerField(help_text="Belgilangan Foiz")
    salary = models.FloatField(help_text="Oylik")
    paid = models.BooleanField(default=False)
    taken = models.BooleanField(default=False)
    center = models.ForeignKey(
        Center, on_delete=models.PROTECT, related_name='monthly_bill')

    def __str__(self):
        return self.name


# class Income(BaseModel):
#     center = models.ForeignKey(Center, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=200)
#     payment_type = models.CharField(max_length=200, choices=PAYMENT_TYPE)
#     price = models.FloatField()

#     def __str__(self):
#         return f"{self.name} {self.price}"


# class Outcome(BaseModel):
#     center = models.ForeignKey(Center, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=200)
#     payment_type = models.OneToOneField(
#         Payment_type, on_delete=models.PROTECT, related_name='outcome')
#     price = models.FloatField()

#     def __str__(self):
#         return f"{self.name} {self.price}"
