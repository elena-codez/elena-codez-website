import os

import django_heroku

from .base import *  # noqa: F401, F403

DEBUG = False  # noqa: F405

MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware"]  # noqa: F405

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # noqa: F405
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

django_heroku.settings(locals())
