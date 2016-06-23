from django.conf.urls import url

from posts.views import *


urlpatterns = [
    url(r'^create/$', PostCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),

]
