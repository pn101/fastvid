from django.views.generic import View
from django.shortcuts import render

from users.models import User


class FollowingListView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                'user/followinglist.html',
                {
                    'site_name': 'Following List',
                    'follower': User.objects.get(username=self.kwargs.get('user_name')),
                }
        )
