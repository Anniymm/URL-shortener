from django.test import TestCase
from .models import URL
class URLModelTests(TestCase):
    def test_generate_short_url(self): # test for unique url
        url = URL(original_url='https://www.example.com')
        short_url = url.generate_short_url()
        self.assertEqual(len(short_url), 6)
        self.assertTrue(short_url.isalnum())  # Check if contains alphanumeric characters

    def test_unique_short_url(self): # Test for duplicated short URLs.
        url1 = URL(original_url='https://www.example1.com')
        url1.save()
        url2 = URL(original_url='https://www.example2.com')
        url2.save()
        self.assertNotEqual(url1.short_url, url2.short_url)

    def test_save_method_generates_short_url(self): # Test that the save method generates a short URL .
        url = URL(original_url='https://www.example.com')
        url.save()
        self.assertIsNotNone(url.short_url)
        self.assertEqual(len(url.short_url), 6)
        self.assertTrue(url.short_url.isalnum())

    def test_str_method(self): # test for string 
        url = URL(original_url='https://www.example.com', short_url='abc123')
        self.assertEqual(str(url), 'https://www.example.com -> abc123')

    def test_no_short_url_on_creation(self):
        url = URL(original_url='https://www.example.com')
        url.save()
        self.assertIsNotNone(url.short_url)
        self.assertEqual(len(url.short_url), 6)
