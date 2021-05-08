"""
ASGI config for main project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'friendship'

    def ready(self):
        import friendship.signals
