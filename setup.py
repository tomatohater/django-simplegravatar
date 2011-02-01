from distutils.core import setup

setup(
    name = 'django-simplegravatar',
    version = '0.2',
    packages = ['simplegravatar', ],
    package_data = {
        'simplegravatar': [
            'templates/templatetags/simplegravatar/*.html',
            'templatetags/*.py'],
    },
    author = 'Drew Engelson',
    author_email = 'drew@engelson.net',
    url = 'http://tomatohater.com/django-simplegravatar/',
    license = 'GPLv3',
    description = 'A simpler Django template tag to add Gravatar support to your Django projects.',
    long_description = 'A simpler Django template tag to add Gravatar support to your Django projects.',
    keywords = 'django avatar gravatar',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)