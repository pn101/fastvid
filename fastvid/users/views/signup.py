from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model


class SignupView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                'user/signup.html',
                {
                    'site_name': 'Signup Page',
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

        return redirect('user:login')
