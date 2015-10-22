import sys
import hashlib
from django.test import TestCase
from django.conf import settings
if sys.version_info[0] == 2:
    from urlparse import urlparse, parse_qs
else:
    from urllib.parse import urlparse, parse_qs
from simplegravatar.templatetags.simplegravatar import show_gravatar, show_gravatar_secure


class SimpleGravatarTest(TestCase):

    def setUp(self):
        super(SimpleGravatarTest, self).setUp()
        self.email = 'test@test.com'
        self.email_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()

    def _set_defaults_settings(self):
        setattr(settings, 'SIMPLEGRAVATAR_SIZE', 80)
        setattr(settings, 'SIMPLEGRAVATAR_RATING', 'g')
        setattr(settings, 'SIMPLEGRAVATAR_DEFAULT', '')
        setattr(settings, 'SIMPLEGRAVATAR_SECURE', False)

    def test_gravatar_default_size(self):
        result = show_gravatar(self.email)
        parsed_url = urlparse(result['gravatar']['url'])
        params = parse_qs(parsed_url.query)
        self.assertIn('size', params)
        self.assertEqual(params.get('size')[0], '80')

    def test_gravatar_modified_size_in_settings(self):
        setattr(settings, 'SIMPLEGRAVATAR_SIZE', 60)
        result = show_gravatar(self.email)
        parsed_url = urlparse(result['gravatar']['url'])
        params = parse_qs(parsed_url.query)
        self.assertIn('size', params)
        self.assertEqual(params.get('size')[0], '60')

    def test_gravatar_modified_size_in_templatetag(self):
        result = show_gravatar(self.email, size=100)
        parsed_url = urlparse(result['gravatar']['url'])
        params = parse_qs(parsed_url.query)
        self.assertIn('size', params)
        self.assertEqual(params.get('size')[0], '100')

    def test_gravatar_default_rating(self):
        result = show_gravatar(self.email)
        parsed_url = urlparse(result['gravatar']['url'])
        params = parse_qs(parsed_url.query)
        self.assertIn('rating', params)
        self.assertEqual(params.get('rating')[0], 'g')

    def test_gravatar_modified_rating_in_settings(self):
        setattr(settings, 'SIMPLEGRAVATAR_RATING', 'x')
        result = show_gravatar(self.email)
        parsed_url = urlparse(result['gravatar']['url'])
        params = parse_qs(parsed_url.query)
        self.assertIn('rating', params)
        self.assertEqual(params.get('rating')[0], 'x')

    def test_gravatar_default_default(self):
        result = show_gravatar(self.email)
        parsed_url = urlparse(result['gravatar']['url'])
        params = parse_qs(parsed_url.query)
        self.assertNotIn('default', params)

    def test_gravatar_default_modified_in_settings(self):
        setattr(settings, 'SIMPLEGRAVATAR_DEFAULT', 'mm')
        result = show_gravatar(self.email)
        parsed_url = urlparse(result['gravatar']['url'])
        params = parse_qs(parsed_url.query)
        self.assertIn('default', params)
        self.assertEqual(params.get('default')[0], 'mm')

    def test_url_ssl_default(self):
        self._set_defaults_settings()
        setattr(settings, 'SIMPLEGRAVATAR_SECURE', True)
        result = show_gravatar(self.email)
        parsed_url = urlparse(result['gravatar']['url'])
        self.assertEqual(parsed_url.scheme, 'https')
        self.assertEqual(parsed_url.netloc, 'secure.gravatar.com')
        params = parse_qs(parsed_url.query)
        self.assertIn('size', params)
        self.assertEqual(params.get('size')[0], '80')
        self.assertIn('rating', params)
        self.assertEqual(params.get('rating')[0], 'g')
        self.assertNotIn('default', params)

    def test_url_ssl_via_templatetag(self):
        self._set_defaults_settings()
        result = show_gravatar_secure(self.email)
        parsed_url = urlparse(result['gravatar']['url'])
        self.assertEqual(parsed_url.scheme, 'https')
        self.assertEqual(parsed_url.netloc, 'secure.gravatar.com')
        params = parse_qs(parsed_url.query)
        self.assertIn('size', params)
        self.assertEqual(params.get('size')[0], '80')
        self.assertIn('rating', params)
        self.assertEqual(params.get('rating')[0], 'g')
        self.assertNotIn('default', params)
