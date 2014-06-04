Development
===========

Required:

 * python-2.7
 * virtualenv
 * fabric

Build:

    # Sometimes need exec `. venv/bin/activate` (just only if don't have cssmin in PATH)
    [ -f smk_resume/settings_local.py ] || cp smk_resume/settings_local{_example,}.py
    fab build
    fab manage:check_permissions

Usage:

    fab run
    # or
    venv/bin/python manage.py runserver

Recomended:

    venv/bin/pip install django-extensions Werkzeug && echo "from settings import INSTALLED_APPS\nINSTALLED_APPS += ('django_extensions', )" >> smk_resume/settings_local.py
    fab r


Production
==========

Required:

 * python-2.7
 * virtualenv
 * uwsgi/gunicorn/...
