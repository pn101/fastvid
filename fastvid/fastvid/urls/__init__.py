from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from users.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^', include('users.urls', namespace='user')),
    url(r'^posts/', include('posts.urls', namespace='posts')),

    url(r'^(?P<user_name>\w+)/$', YourPageView.as_view(), name='yourpage'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
