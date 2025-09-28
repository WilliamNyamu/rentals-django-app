from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip= False,
        widget= forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Password Confirmation",
        strip=False,
        widget= forms.PasswordInput
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'phone_number') # we do not include password field here.


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'is_active', 'is_superuser', 'is_staff')

