from django.views.generic import View

from tags.models import Tag


class TagBaseView(View):
    model = Tag
    slug_field = 'name'
