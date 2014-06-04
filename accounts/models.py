from django.db import models
from django.contrib.auth.models import User  
from django.utils.translation import ugettext as _  
from userena.models import UserenaBaseProfile  


class MyProfile(UserenaBaseProfile):  
    user = models.OneToOneField(User, unique=True,
        verbose_name=_('user'), related_name='my_profile')
    burn_date = models.DateField(_('Burn Date'), null=True,
        help_text="Enter you burn date (format: YEAR-MONTH-DAY)")
    mob_phone = models.CharField(_('Mobile Phone'), null=True, max_length=20,
        blank=True, help_text="Enter you phone number (format: 099-0005500)")
