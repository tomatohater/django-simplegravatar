import sys
import hashlib

from django import template
from django.conf import settings

if sys.version_info[0] == 2:
    from urllib import urlencode
else:
    from urllib.parse import urlencode

register = template.Library()


@register.inclusion_tag('templatetags/simplegravatar/image.html')
def show_gravatar(email, size=None, ssl=False):
    '''
    An inclusion tag that inserts gravatar image.
    '''

    size = size or getattr(settings, 'SIMPLEGRAVATAR_SIZE', 80)
    rating = getattr(settings, 'SIMPLEGRAVATAR_RATING', 'g')
    default = getattr(settings, 'SIMPLEGRAVATAR_DEFAULT', '')
    ssl = ssl or getattr(settings, 'SIMPLEGRAVATAR_SECURE', False)

    gravatar_base = 'http://www.gravatar.com/avatar'
    if ssl:
        gravatar_base = 'https://secure.gravatar.com/avatar'

    url = "%s/%s.jpg?%s" % (gravatar_base,
                            hashlib.md5(email.encode('utf-8')).hexdigest(),
                            urlencode({
                                'size': str(size),
                                'rating': rating,
                                'default': default,
                            }))

    return {
        'gravatar': {
            'url': url, 'size': size
        }
    }


@register.inclusion_tag('templatetags/simplegravatar/image.html')
def show_gravatar_secure(email, size=None):
    '''
    An inclusion tag that inserts gravatar image (over https).
    '''
    return show_gravatar(email, size, True)
