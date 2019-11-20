from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import Employee


@admin.register(Employee)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('id', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id', 'card_id', 'first_name', 'last_name', 'email', 'mobile_number', 'password1', 'password2'),
        }),
    )
    list_display = ('id', 'first_name', 'last_name', 'is_staff')
    search_fields = ('id', 'first_name', 'last_name')
    ordering = ('id',)
