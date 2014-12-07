import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def extended_markdown(s):
    '''
    Render markdown, with nice extensions.
    '''
    extensions = [
        'nl2br',  # More intuitive linebreak
        'smarty',  # emdash, endash, pretty quotes
    ]

    return mark_safe(markdown.markdown(force_unicode(s),
                                       extensions,
                                       safe_mode=True,
                                       enable_attributes=False))


# Modified from https://djangosnippets.org/snippets/2428/
@register.tag
def add_get(parser, token):
    '''
    Add GET parameters to the current url.

    - Values for GET parameters can be strings or variables
      (if variables, they will be resolved before becoming GET params).
    - Keys and values subject to changes by urlencode().
    - If keys already exist in the current url, they will be replaced
      with the new values.
    - To remove a key from the url, just put no value after the equals.

    Usage:
        {% url "topic='bread'" %}           # set to a constant
        {% url "topic=var.field" %}         # set to a variable
        {% url "page=" %}                   # remove key from url
        {% url "topic='bread' page=1" %}    # set more than one

    Modified from https://djangosnippets.org/snippets/2428/
    '''
    # Ensure one argument
    try:
        tag_name, arg = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument" % token.contents.split()[0])

    # Ensure that the argument is properly surrounded by quotes
    if not (arg[0] == arg[-1] and arg[0] in ('"', "'")):
        raise template.TemplateSyntaxError(
            "%r tag's argument should be in quotes" % tag_name)

    pair_list = arg[1:-1].split()
    pair_dict = {}
    for pair in pair_list:
        s = pair.split('=', 1)
        pair_dict[s[0]] = parser.compile_filter(s[1])

    return AddGetNode(pair_dict)


class AddGetNode(template.Node):
    def __init__(self, new_values):
        self.new_values = new_values

    def render(self, context):
        request = template.resolve_variable('request', context)
        params = request.GET.copy()

        for key, value in self.new_values.items():
            resolved = value.resolve(context)
            if resolved:
                params[key] = resolved
            elif key in params:
                del params[key]

        return '?%s' % params.urlencode()
