from django.test import TestCase, SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):
    def index_test_page_status(self):
        response = self.client.get('/apps')
        self.assertEquals(response.status_code, 200)