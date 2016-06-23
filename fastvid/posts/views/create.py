from django.views.generic import View
from django.shortcuts import render, redirect

from posts.utils import youtube


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

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        video_id = request.POST.get('video_id')
        content = request.POST.get('content')

        return render(
                request,
                'post/create_confirm.html',
                {
                    'site_name': 'Confirm Post',
                    'title': title,
                    'video_id': video_id,
                    'content': content,

                    'youtube_original_url': youtube.get_youtube_original_url(video_id),
                    'youtube_embed_url': youtube.get_youtube_embed_url(video_id),
                }
        )
