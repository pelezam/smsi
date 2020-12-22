from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Personnel, Fonction

admin.site.register(Fonction)


@admin.register(Personnel)
class PersonnelAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Personnel
    list_display = ('username', 'last_name', 'first_name')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('last_name', 'first_name', 'username', 'sexe', 'contact', 'fonction', 'photo', 'password1', 'password2'),
        }),
    )
