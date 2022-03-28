from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class MyUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'is_staff', 'is_active']
    
admin.site.register(User, MyUserAdmin)