import datetime
import calendar

from django.db.models import Sum, Q, Count, Prefetch
from django.db.models.functions import TruncMonth
from django.shortcuts import render
from branch.models import Branch
from users.models import User
from finance.models import Transaction


def dashboard(request):
    today = datetime.datetime.today()
    year = datetime.datetime.now().year
    last_month = datetime.datetime.now().month-1

    income = sum(Transaction.objects.filter(
        paid_at__month=last_month, type='income').values_list('amount', flat=True))
    total_students = User.objects.filter(role='student').count()
    expense = sum(Transaction.objects.filter(
        paid_at__month=last_month, type='expense').values_list('amount', flat=True))

    income_branches = Branch.objects.prefetch_related(
        Prefetch(
            'transactions', Transaction.objects.filter(
                type="income"))
    ).annotate(total_income=Sum('transactions__amount'))
    expense_branches = Branch.objects.prefetch_related(
        Prefetch(
            'transactions', Transaction.objects.filter(
                type="expense"))
    ).annotate(total_income=Sum('transactions__amount'))
    payment_channels = Transaction.objects.filter(
        paid_at__month=last_month, type='income').values_list('center', flat=True)
    branches = Branch.objects.annotate(total_loans=Sum('loan'))    
    users_bdays = User.objects.filter(created_data=today)

    branches = Branch.objects.count()

    context = {
        'branches': branches,
        'total_students': total_students,
        # 'incomes': total_amount,

    }
    return render(request, 'home/index.html', context)


def learning_center(request):
    #     Курслар
    # 2. Гурухлар
    # 3. Ўқувчилар
    # 4. Ўқитувчилар
    # 5. Тўловлар тариҳи
    # 6. Чикимлар
    # 7. Ойлик хисоб-китоб
    center = Center.objects.get(id=1)
    courses = center.courses.all()
    groups = center.group.all()
    teachers = center.user_group.filter(role="teacher") # !!!
    students = center.courses.group.user_group.filter(role="student") # !!!
    payment_history = center.payment_history.all()
    # organish bitta model yaratilganda avtomatik boshqa model yaratilib ketishi kerak