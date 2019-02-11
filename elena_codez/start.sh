#!/bin/bash

python manage.py collectstatic --no-input
gunicorn config.wsgi --bind 0.0.0.0:8000
