from django.contrib import admin
from .models import User

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm#, SignUpForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email','is_shop','is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Разрешения', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',) 
    # def delete_model(self, request, queryset):
    #     for obj in queryset:
    #         print(obj)
    #         obj.delete()
    # actions=[delete_model]


admin.site.register(User, CustomUserAdmin)