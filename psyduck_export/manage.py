#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'psyduck_export.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    try:
        import psyduck_export.view
        psyduck_export.view.dispose_all()
        psyduck_export.view.time_thread_start()
        main()
    except InterruptedError:
        import psyduck_export.view

        psyduck_export.view.dispose_all()
