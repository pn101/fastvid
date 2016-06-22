from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTestCase(TestCase):

    def test_user_model_for_phonenumber(self):
        user = get_user_model().objects.create_user(
                username='username',
                password='password',
                phonenumber='01234567890',
        )

        self.assertTrue(
                user.phonenumber,
        )
