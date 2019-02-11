import os

import django_heroku

from .base import *  # noqa: F401, F403

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # noqa: F405

django_heroku.settings(locals())
