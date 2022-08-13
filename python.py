


import django
import sys
import os

# ---------  Setup django  //  --------------
path_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

import datetime
from center.models import Center
from datetime import timedelta
from users.models import User
from django.db.models import Sum, Prefetch
from branch.models import Branch
from finance.models import Transaction
from django.utils import timezone

# ---------  //  Setup django  --------------
year = datetime.datetime.now().year
last_month = datetime.datetime.now().month-1
# income_branches = Branch.objects.prefetch_related(
#     Prefetch(
#         'transactions', Transaction.objects.filter(
#             type="income"))
# ).annotate(total_income=Sum('transactions__amount'))
# for income in income_branches:
#     print(f"{income.name} ___ {income.total_income}")

# payment_channels = Transaction.objects.filter(
#     paid_at__month=last_month, type='income').values_list('center', flat=True)
# print(payment_channels)

# for branch in branches:
#     print(branch.total_loans)


# print(Center.courses.values('name'))
center = Center.objects.get(id=1)
# print(center.courses.all())

teachers = center.
# print(teachers.name)