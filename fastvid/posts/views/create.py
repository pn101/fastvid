from django.views.generic import View
from django.shortcuts import render, redirect


class PostCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                'post/create.html',
                {
                    'site_name': 'Post Create',
                }
        )


class PostCreateConfirmView(View):
    pass
