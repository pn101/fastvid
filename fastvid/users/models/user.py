from django.db import models
from django.contrib.auth.models import AbstractUser

from .follow import Follow


class User(AbstractUser):

    phonenumber = models.CharField(
            max_length=16,
    )

    follower_set = models.ManyToManyField(
            'self',
            symmetrical=False,
            related_name='following_set',
            through=Follow,
            through_fields=('following', 'follower'),
    )

    class Meta:
        permissions = (
                ('can_create_post', 'can create post'),
        )
