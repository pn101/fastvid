from django.apps import AppConfig


class NotificationsConfig(AppConfig):

    name = 'notifications'

    def ready(self):
        from notifications.signals.post_save import post_save_notification
