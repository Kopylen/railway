from django import template
from django.db.models import Count

from homee.models import TagPost

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.inclusion_tag('list_tags.html')
def get_all_tags():
    return {'tags': TagPost.objects.annotate(total=Count("tags")).filter(total__gt=0)}
