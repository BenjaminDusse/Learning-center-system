import datetime
from users.models import User


now = datetime.datetime.now()
today, month = now.day, now.month
tomorrow = now + datetime.timedelta(days=1)
tomorrow_day, tomorrow_month = tomorrow.day, tomorrow.month

birth_day_today = User.objects.filter(
    date_of_birth__day=today, date_of_birth__month=month).order_by('username')
birth_day_tomorrow = User.objects.filter(
    date_of_birth__day=tomorrow_day, date_of_birth__month=tomorrow_month).order_by('username')