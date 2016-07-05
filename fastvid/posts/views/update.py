from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy

from posts.models import Post
from .base import PostBaseView


class PostUpdateView(PostBaseView, UpdateView):
    template_name = 'post/update.html'
    fields = [
        'title',
        'video_id',
        'content',
    ]

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['site_name'] = 'Update Post'
        context['post'] = Post.objects.get(hash_id=self.kwargs.get('slug'))
        return context
