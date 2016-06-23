from django.db import models
from django.core.urlresolvers import reverse

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

    def get_absolute_url(self):
        return reverse(
                'posts:detail',
                kwargs={
                    'pk': self.id,
                }
        )

    def get_youtube_original_url(self):
        from posts.utils import get_youtube_original_url as get_video_url
        return get_video_url(self.video_id)
    youtube_original_url = property(get_youtube_original_url)

    def get_youtube_embed_url(self):
        return 'https://www.youtube.com/embed/{video_id}'.format(
                video_id=self.video_id
        )
