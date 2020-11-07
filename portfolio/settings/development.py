from .base import *

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


INSTALLED_APPS += [
    "django_extensions",
]

sqlite = {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR.parent / "db.sqlite3",
}

if os.getenv("SQL", None) is None:
    DATABASES = {"default": sqlite}


STATIC_URL = "/static/"

STATICFILES_DIRS = [Path.joinpath(BASE_DIR, "static", "portfolio")]

STATIC_ROOT = Path.joinpath(BASE_DIR, "static")

MEDIA_URL = "/media/"
# DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

MEDIA_ROOT = Path.joinpath(BASE_DIR, "media")