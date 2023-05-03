from .base import *

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = env("EMAIL_PORT")
DEFUALT_FROM_EMAIL = "info@real_estate.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "REAL ESTATE"


DATABASES = {
    "default": {
        "ENGINE": env("ENGINE"),
        "NAME": env("NAME"),
        "USER": env("USER"),
        "PASSWORD": env("PASSWORD"),
        "HOST": env("HOST"),
        "PORT": env("PORT"),
        "OPTIONS": {
            "charset": "utf8mb4"
        }
    }
}
