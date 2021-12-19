from django import template

register = template.Library()


@register.filter(name='get_list')
def get_list(number):
    return range(number)
