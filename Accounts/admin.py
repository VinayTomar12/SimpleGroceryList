from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'get_full_name', 'staff', 'is_active', 'last_login')
    search_fields = ('email', 'first_name', 'last_name')
# # admin.site.unregister(User)

admin.site.register(User, UserAdmin)