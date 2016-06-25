from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from users.models import User


class YourPageView(View):

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs.get('user_name'))
        if user != request.user:
            return render(
                    request,
                    'user/yourpage.html',
                    {
                        'site_name': 'Your Page',
                        'username': user.username,
                        'posts': user.post_set.all(),
                    }
            )
        return redirect('user:mypage')
