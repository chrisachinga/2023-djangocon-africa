from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_verified', 'phone_number', 'gender', 'year_of_birth')
    list_filter = ('is_verified', 'gender')
    search_fields = ('username', 'email', 'phone_number')

admin.site.register(User, UserAdmin)
