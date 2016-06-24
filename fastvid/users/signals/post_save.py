from django.db.models.signals import post_save
from django.dispatch import receiver

from users.utils import send_sms
from users.models import User


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        send_sms(
            sender='01022205736',
            receiver=instance.phonenumber,
            content='Thank you for registering with us, {name}'.format(
                name=instance.first_name,
            ),
        )
