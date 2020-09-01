from django.test import SimpleTestCase
from django.urls import reverse


class TestCoreViews(SimpleTestCase):

    def test_root_view(self):
        """
        Make sure the root url point to the default homepage
        """
        response = self.client.get(reverse('core:root'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')
