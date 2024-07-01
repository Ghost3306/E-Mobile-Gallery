

from django import template

register = template.Library()

@register.filter(name='mul')
def mul(value, arg):
    try:
        print(value)
        print(arg)
        return int(value) * int(arg)
    except (ValueError, TypeError) as e:
        print(e)
        return None
