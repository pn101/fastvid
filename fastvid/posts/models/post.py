from django.db import models

from users.models import User


class Post(models.Model):

    user = models.ForeignKey(User)

    hash_id = models.CharField(
            max_length=6,
    )

    video_id = models.CharField(
            max_length=16,
    )

    video_title = models.CharField(
            max_length=256,
            blank=True,
            null=True,
    )

    title = models.CharField(
            max_length=256,
    )

    content = models.TextField()

    def __str__(self):
        return self.title
