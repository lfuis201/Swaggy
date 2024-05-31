# custom_filters.py

from django import template

register = template.Library()

@register.filter
def stars_to_emojis(stars):
    # Convierte el número de estrellas en emojis
    return '⭐' * int(stars)
