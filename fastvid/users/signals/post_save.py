from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User
from users.tasks import SimpleTask


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        sms = SimpleTask()
        sms.run(instance)
