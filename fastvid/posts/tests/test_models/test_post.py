from django.test import TestCase
from django.contrib.auth import get_user_model


class PostModelTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
                username='username',
                password='password',
                phonenumber='00011112222',
        )

        self.test_video_id = 'fastvid'

        self.post = self.user.post_set.create(
                title='test_title',
                video_id=self.test_video_id,
        )

    def test_post_for_youtube_original_url(self):
        youtube_original_url = 'https://www.youtube.com/watch?v={video_id}'.format(
                video_id=self.test_video_id,
        )
        self.assertEqual(
                self.post.get_youtube_original_url(),
                youtube_original_url,
        )
