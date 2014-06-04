from django import forms
from django.utils.translation import ugettext_lazy as _
from userena.forms import SignupForm
from captcha.fields import CaptchaField
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class SignupFormExtra(SignupForm):
    captcha = CaptchaField()

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        print(password)
        if len(password) < 6:
            raise ValidationError('Password too short')
        if len(password) > 16:
            raise ValidationError('Password too long')
        return password
