from django import template
register = template.Library()

@register.simple_tag
def filter(qs, **kwargs):
    return qs.filter(**kwargs)