from django.views.generic import View
from django.shortcuts import render, redirect

from users.models import User, Follow


class FollowView(View):

    def get(self, request, *args, **kwargs):
        follower = self.request.user
        following = User.objects.get(username=self.kwargs.get('user_name'))

        if follower != following:
            Follow.objects.get_or_create(
                    follower=follower,
                    following=following,
            )
            return render(
                    request,
                    'user/follow_confirm.html',
                    {
                        'site_name': 'Follow Confirm',
                        'follower': follower,
                        'following': following,
                    }
            )
        return redirect('user:mypage')
