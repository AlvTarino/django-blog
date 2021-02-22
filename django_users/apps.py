from django.apps import AppConfig


class DjangoUsersConfig(AppConfig):
    name = 'django_users'

    def ready(self):
        import django_users.signals

