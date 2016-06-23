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

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        video_id = request.POST.get('video_id')
        content = request.POST.get('content')

        post = request.user.post_set.create(
                title=title,
                video_id=video_id,
                content=content,
        )

        return redirect(post)


class PostCreateConfirmView(View):
    pass
