from django.db import models
from django.contrib.auth.models import User  
from django.utils.translation import ugettext as _  
from userena.models import UserenaBaseProfile
from django.core.validators import RegexValidator


class MyProfile(UserenaBaseProfile):  
    user = models.OneToOneField(User, unique=True,
        verbose_name=_('user'), related_name='my_profile')
    burn_date = models.DateField(_('Burn Date'), null=True,
        help_text="format: YEAR-MONTH-DAY")
    mob_phone = models.CharField(_('Mobile Phone'), null=True, max_length=20,
        validators = [
            RegexValidator(
                r'^\([0-9]{3}\) [0-9]{3}-[0-9]{1,4}$',
                message="Wrong format"
            ),
        ],
        blank=True, help_text="format: (099) 555-1234")
