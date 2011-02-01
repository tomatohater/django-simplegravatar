==================================================
django-simplegravatar (version 0.2)
http://tomatohater.com/django-simplegravatar/
Last updated: 31-Jan-2011
==================================================

DESCRIPTION:
A simpler Django template tag to add Gravatar support to your Django projects.


INSTALLATION:
To install this app, simply:
    1) pip install django-simplegravatar
        or drop the 'simplegravatar' folder somewhere on your PYTHONPATH
    2) Add 'simplegravatar' to your projects INSTALLED_APPS list in settings.py

    Optional settings:

    SIMPLEGRAVATAR_SIZE (default: 80)
    - Pixel width and height of Gravatar (they are all square)
        
    SIMPLEGRAVATAR_RATING (default: 'g')
    - g, pg, r, x   
        
    SIMPLEGRAVATAR_DEFAULT (default: '')
    - Default image if no Gravatar exists for email. Should be a full image
      URL to your custom image, or one of the Gravatar built-in defaults...  
        - 404: do not load any image if none is associated with the email
          hash, instead return an HTTP 404 (File Not Found) response
        - mm: (mystery-man) a simple, cartoon-style silhouetted outline of a
          person (does not vary by email hash)
        - identicon: a geometric pattern based on an email hash
        - monsterid: a generated 'monster' with different colors, faces, etc
        - wavatar: generated faces with differing features and backgrounds
        - retro: awesome generated, 8-bit arcade-style pixelated faces
            
    SIMPLEGRAVATAR_SECURE (default: False)
    - Use https?
    
    For more information about these default options see:
    http://en.gravatar.com/site/implement/images/


USAGE (this goes in your templates):
    {% load simplegravatar %}
    {% show_gravatar "email@address.com" %}

You may optionally pass a size into this tempalte tag:
    {% show_gravatar "email@address.com" 48 %}
    
If you require a secure image (instead of using SETTINGS):
    {% show_gravatar_secure "email@address.com" %}


Send bugs, questions, comments, and/or beer to:
Drew Engelson <drew@engelson.net>

Enjoy!


