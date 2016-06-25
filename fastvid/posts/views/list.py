from django.views.generic.list import ListView

from .base import PostBaseView


class PostListView(PostBaseView, ListView):
    template_name = 'post/list.html'
    context_object_name = 'posts'
