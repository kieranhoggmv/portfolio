from django import template
from django.template.defaultfilters import stringfilter

from web.views import KSBS

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def highlight(text):
    for key in KSBS:
        if (
            f"[{key}]" in text
            or f"({key})" in text
            or f"/{key}" in text
            or f"{key}/" in text
            or f"{key}+" in text
            or f"{key}]" in text
        ):
            text = text.replace(key, f"<span class='highlight'>{key}</span>")
    return text
