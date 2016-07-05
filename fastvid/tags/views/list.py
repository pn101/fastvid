from django.views.generic import View
from django.shortcuts import render

from .base import TagBaseView
from tags.models import Tag


class TagListView(TagBaseView, View):

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        tag_list = Tag.objects.all()

        if search:
            tag_list = list(filter(
                lambda tag: search.lower() in tag.name.lower(),
                tag_list,
            ))

        return render(
                request,
                'tags/list.html',
                {
                    'site_name': 'Search Tag',
                    'tag_list': tag_list,
                }
        )
