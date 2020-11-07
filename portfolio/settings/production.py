from .base import *

DEBUG = os.environ.get("DEBUG", False)

DATABASES = {}
DATABASES["default"] = dj_database_url.config(conn_max_age=600)


INSTALLED_APPS += [
    "django_extensions",
    "cloudinary_storage",
    "cloudinary",
]

SECURE_SSL_REDIRECT = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

ALLOWED_HOSTS = [
    "hpca01portfolio.herokuapp.com",
    "hpca01.info",
]  # TODO: to be amended


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_URL = "/static/"

# STATICFILES_DIRS = [Path.joinpath(BASE_DIR, "static", "portfolio")]

STATIC_ROOT = Path.joinpath(BASE_DIR.parent, "static")

MEDIA_URL = "/media/"
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

MEDIA_ROOT = Path.joinpath(BASE_DIR.parent, "media")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "DEBUG"),
        },
    },
}

# This should already be in your settings.py
django_heroku.settings(locals(), logging=False)  # This is new

options = DATABASES["default"].get("OPTIONS", {})

options.pop("sslmode", None)  # type: ignore

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_NAME"),
    api_key=os.getenv("CLOUDINARY_KEY"),
    api_secret=os.getenv("CLOUDINARY_SECRET"),
)