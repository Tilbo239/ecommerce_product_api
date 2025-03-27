from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'imageprofile', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Profile Picture', {'fields': ('imageprofile',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Profile Picture', {'fields': ('imageprofile',)}),
    )

admin.site.register(CustomUser)


