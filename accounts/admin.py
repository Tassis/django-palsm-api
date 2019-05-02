from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from accounts.forms import AccountChangeForm, AccountCreationForm
from accounts.models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    model = Account
    list_display = ['email', 'username', 'date_joined', 'profile_count']


admin.site.register(Account, AccountAdmin)