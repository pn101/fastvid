from django.conf.urls import url

from users.views import *


urlpatterns = [
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^premiumsignup/$', PremiumSignupView.as_view(), name='premium'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^mypage/$', MyPageView.as_view(), name='mypage'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^(?P<user_name>\w+)/$', YourPageView.as_view(), name='yourpage'),
    url(r'^(?P<user_name>\w+)/follow/$', FollowView.as_view(), name='follow'),

]
