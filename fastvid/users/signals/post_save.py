from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User
from users.tasks import SimpleTask
from notifications.models import SMSNotification


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        sms = SMSNotification.objects.create(
                sender='01031186228',
                receiver=instance.phonenumber,
                content='Hello and thanks for registering',
        )
