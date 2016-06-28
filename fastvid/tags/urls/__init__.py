from django.conf.urls import url

from tags.views import *


urlpatterns = [
    url(r'^(?P<slug>\w+)/$', TagDetailView.as_view(), name='detail'),

]
