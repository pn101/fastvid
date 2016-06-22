from django.views.generic import View
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)

        messages.add_message(
                request,
                messages.SUCCESS,
                settings.LOGOUT_SUCCESS_MESSAGE,
        )
        return redirect('user:login')
