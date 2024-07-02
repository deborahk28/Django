import os
import sys
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'office.settings')

if __name__ == "__main__":
    # Add the '--noreload' argument if 'runserver' is in sys.argv
    if 'runserver' in sys.argv:
        sys.argv.append('--noreload')
    execute_from_command_line(sys.argv)
