from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import SafeText

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def smart_truncate(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix
