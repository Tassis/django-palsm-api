from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import Account

class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ( 'email', 'last_name', 'password')


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = UserChangeForm.Meta.fields