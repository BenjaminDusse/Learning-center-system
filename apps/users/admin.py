from django.contrib import admin
from users.models import User, Role, UserActivity

admin.site.register(User)
admin.site.register(Role)
admin.site.register(UserActivity)

