from django.conf.urls import url

from tags.views import *


urlpatterns = [
    url(r'^$', TagListView.as_view(), name='list'),
    url(r'^add/$', TagAddView.as_view(), name='add'),
    url(r'^(?P<slug>\w+)/$', TagDetailView.as_view(), name='detail'),

]
