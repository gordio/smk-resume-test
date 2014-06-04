from django import forms
from userena.forms import SignupForm
from captcha.fields import CaptchaField


class SignupFormExtra(SignupForm):
    captcha = CaptchaField()
