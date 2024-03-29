from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from accounts.forms import SignupFormExtra


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),

    url(r'^accounts/signup/$', 'userena.views.signup',
        {'signup_form': SignupFormExtra}),
    url(r'^accounts/', include('userena.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


# Apply media file for development
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
