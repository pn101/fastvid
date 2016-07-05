from django.conf.urls import url

from posts.views import *


urlpatterns = [
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^create/$', PostCreateView.as_view(), name='create'),
    url(r'^confirm/$', PostCreateConfirmView.as_view(), name='confirm'),
    url(r'^(?P<slug>\w+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>\w+)/update/$', PostUpdateView.as_view(), name='update'),

]
