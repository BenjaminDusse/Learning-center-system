import calendar

from django.db.models import Sum, Q, Count
from django.db.models.functions import TruncMonth

def income_statistics(queryset, year):

    data = queryset.filter(paid_at__year=year).values('paid_at__month').annotate(
        sum=Sum('amount'), month=TruncMonth('paid_at')).order_by()
    date = list(map(lambda x: x, calendar.month_name))[1:]
    temp = list(0 for _ in range(len(date)))
    k = -1
    for item in date:
        k += 1
        for i in data:
            if item == i['month'].strftime("%B"):
                temp[k] = i['sum']

    data_json = {
        'labels': date,
        'series': {
            'type': 'bar',
            "data": temp
        },
    }

    return data_json
