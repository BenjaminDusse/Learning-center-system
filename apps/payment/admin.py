from django.contrib import admin
from payment.models import *


admin.site.register(Payment_type)
admin.site.register(Payment_history)
admin.site.register(Loan)
admin.site.register(Monthly_Bill)
admin.site.register(Income)
admin.site.register(Outcome)
