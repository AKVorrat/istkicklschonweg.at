import re
from django import template
from django.forms.fields import CheckboxInput

register = template.Library()

@register.filter(name='field_type')
def field_type(field, ftype):
    try:
        t = field.field.widget.__class__.__name__
        return t.lower() == ftype
    except:
        pass
    return False

pattern = re.compile(r'iphone|ipod|android|blackberry|mini|windows|palm')

@register.filter(name='is_mobile')
def is_mobile(request):
    return pattern.search(get_user_agent(request))

def get_user_agent(request):
    return request.META['HTTP_USER_AGENT'].lower()
