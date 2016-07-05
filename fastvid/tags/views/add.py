from django.views.generic import View
from django.shortcuts import redirect

from .base import TagBaseView
from posts.models import Post
from tags.models import Tag


class TagAddView(TagBaseView, View):

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        hash_id = request.POST.get('hash_id')
        post = Post.objects.get(hash_id=hash_id)

        tag = Tag.objects.get_or_create(name=name)

        tag[0].post_set.add(post)

        return redirect(post)
