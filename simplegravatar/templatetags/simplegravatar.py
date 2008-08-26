import urllib, hashlib
from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('templatetags/simplegravatar/image.html')
def show_gravatar(email):
    (size, default, rating) = (80, '', 'G')

    if settings.SIMPLEGRAVATAR_SIZE:
        size = settings.SIMPLEGRAVATAR_SIZE
        
    if settings.SIMPLEGRAVATAR_RATING:
        rating = settings.SIMPLEGRAVATAR_RATING
    
    if settings.SIMPLEGRAVATAR_DEFAULT:
        default = settings.SIMPLEGRAVATAR_DEFAULT
     
    url = "http://www.gravatar.com/avatar/%s.jpg?" % hashlib.md5(email).hexdigest()
    url += urllib.urlencode({
        'size': str(size),     # size
        'rating': rating,        # rating
        'default': default,       # default
    })

    return {'gravatar': {'url': url, 'size': size}}
