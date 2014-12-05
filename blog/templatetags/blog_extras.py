import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def extended_markdown(s):
    extensions = [
        'nl2br',  # More intuitive linebreak
        'smarty',  # emdash, endash, pretty quotes
    ]

    return mark_safe(markdown.markdown(force_unicode(s),
                                       extensions,
                                       safe_mode=True,
                                       enable_attributes=False))
