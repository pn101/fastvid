from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from posts.models import Post


class PremiumSignupView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                'user/premiumsignup.html',
                {
                    'site_name': 'Premium Signup',
                }
        )

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')

        user = get_user_model().objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                phonenumber=phonenumber,
        )

        permission = Permission.objects.get(
                codename='can_create_post',
        )

        user.user_permissions.add(permission)

        return redirect('user:login')

    def get_context_data(self, **kwargs):
        context = super(PremiumSignupView, self).get_context_data(**kwargs)
        context['site_name'] = 'Premium Signup'
        return context
