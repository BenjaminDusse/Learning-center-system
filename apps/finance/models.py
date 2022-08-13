from django.db.models import DecimalField, CharField, ForeignKey, CASCADE, DateField, SET_NULL
from center.models import Center
from contact.models import Contact
from shared.django.model import BaseModel
from branch.models import Branch


class Transaction(BaseModel):
    """
    Transaction
    """
    INCOME = 'income'
    EXPENSE = 'expense'

    TYPE = (
        (INCOME, 'income'),
        (EXPENSE, 'expense'),
    )

    CASH = 'Naqd'
    PLASTIC_CARD = 'Plastik kartochka'
    MONEY_TRANSFER = "Pul o'tkazish"

    PAYMENT_TYPE = (
        (CASH, "Cash"),
        (PLASTIC_CARD, "Plastic Card"),
        (MONEY_TRANSFER, "Money Transfer")
    )

    client = ForeignKey(Contact, CASCADE, null=True, blank=True)
    branch = ForeignKey(Branch, CASCADE, related_name="transactions")
    paid_at = DateField()
    amount = DecimalField(max_digits=15, decimal_places=2)
    type = CharField(max_length=25, choices=TYPE)
    description = CharField(max_length=512)
    center = ForeignKey(Center, on_delete=CASCADE)

    class Meta:
        ordering = ['-created_date']

    @property
    def get_client(self):
        return self.client.full_name

    def __str__(self):
        return self.description
