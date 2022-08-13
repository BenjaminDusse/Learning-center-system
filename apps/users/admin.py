from django.contrib import admin
from django.contrib.auth.models import Group
from contact.models import Contact
from users.models import User, UserGroup
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions', 'language', 'theme', 'role', 'group', 'saldo', 'date_of_birth')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    list_display = ('id', 'username', 'is_staff', 'date_of_birth',
                    'is_superuser')
    list_editable = ('is_staff', 'is_superuser')


admin.site.register(UserGroup)
admin.site.unregister(Group)
