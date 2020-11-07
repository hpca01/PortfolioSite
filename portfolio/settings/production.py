from .base import *

DEBUG = False

DATABASES = {}
DATABASES["default"] = dj_database_url.config(conn_max_age=600)


INSTALLED_APPS += [
    "django_extensions",
]

ALLOWED_HOSTS = [
    "hpca01portfolio.herokuapp.com",
    "hpca01.info",
]  # TODO: to be amended


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_URL = "/static/"

# STATICFILES_DIRS = [Path.joinpath(BASE_DIR, "static", "portfolio")]

STATIC_ROOT = Path.joinpath(BASE_DIR, "static")

MEDIA_URL = "/media/"
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

MEDIA_ROOT = Path.joinpath(BASE_DIR, "media")


# This should already be in your settings.py
django_heroku.settings(locals())  # This is new

options = DATABASES["default"].get("OPTIONS", {})

options.pop("sslmode", None)  # type: ignore

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_NAME"),
    api_key=os.getenv("CLOUDINARY_KEY"),
    api_secret=os.getenv("CLOUDINARY_SECRET"),
)