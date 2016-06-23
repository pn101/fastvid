from django.conf.urls import url

from posts.views import *


urlpatterns = [
    url(r'^create/$', PostCreateView.as_view(), name='create'),

]
