from django import forms
from django.utils.translation import ugettext_lazy as _
from userena.forms import SignupForm
from captcha.fields import CaptchaField
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class SignupFormExtra(SignupForm):
    first_name = forms.CharField(label=_('First name'), max_length=30,
        required=True)
    last_name = forms.CharField(label=_('Last name'), max_length=30,
        required=True)
    burn_date = forms.DateField(label=_('Burn date'), required=True,
        help_text="format: YEAR-MONTH-DAY")
    mob_phone = forms.CharField(label=_('Phone'), required=True,
        validators = [
            RegexValidator(
                r'^\([0-9]{3}\) [0-9]{3}-[0-9]{1,4}$',
                message="Wrong format"
            ),
        ],
        help_text='format: (099) 555-1234')
    captcha = CaptchaField()

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        print(password)
        if len(password) < 6:
            raise ValidationError('Password too short')
        if len(password) > 16:
            raise ValidationError('Password too long')
        return password

    def save(self):
        new_user = super(SignupFormExtra, self).save()

        new_user.first_name = self.cleaned_data['first_name']
        new_user.last_name = self.cleaned_data['last_name']
        new_user.burn_date = self.cleaned_data['burn_date']
        new_user.mob_phone = self.cleaned_data['mob_phone']
        new_user.save()

        return new_user
