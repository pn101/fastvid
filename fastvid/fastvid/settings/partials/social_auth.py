import os


AUTHENTICATION_BACKENDS = [
    'social.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')

SOCIAL_AUTH_REDIRECT_LOGIN = '/mypage/'
