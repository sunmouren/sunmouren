from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserDetailForm(ModelForm):
    class Meta:
        model = User
        fields = ('nickname', 'signature', 'avatar')


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
