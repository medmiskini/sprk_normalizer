from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "sprk_normalizer.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import sprk_normalizer.users.signals  # noqa: F401
        except ImportError:
            pass
