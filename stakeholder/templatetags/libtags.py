from django import template

register = template.Library()

@register.filter
# def space_to_underscore(value):
#     return value.replace(" ", "_")

def to_class(text):
    return text.replace(' ', '_').replace('(', '').replace(')', '')
