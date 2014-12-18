#!/usr/bin/env python
import os
import sys

#django_base_path = os.path.dirname(__file__) 
#print os.path.join(django_base_path, 'static')

# reminder for myself
# django is ran from manage.py, not settings.py
# so os.path.dirname(__file__) would return the path of manage.py


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "polling.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)