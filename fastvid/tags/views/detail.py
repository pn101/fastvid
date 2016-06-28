from django.views.generic.detail import DetailView

from tags.models import Tag
from .base import TagBaseView


class TagDetailView(TagBaseView, DetailView):
    template_name = 'tags/detail.html'
