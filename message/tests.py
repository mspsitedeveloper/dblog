from django.test import SimpleTestCase
from django.urls import reverse

class MessagePageTests(SimpleTestCase):
    def test_url_exzist(self):
        response = self.client.get("/message")
        self.assertEqual(response.status_code, 200)
    def test_url_name(self):
        response = self.client.get(reverse("message"))
        self.assertEqual(response.status_code, 200)
    def test_template_name(self):
        response = self.client.get(reverse("message"))
        self.assertTemplateUsed(response, 'message.html')
    def test_template_content(self):
        response = self.client.get("/message")
        self.assertContains(response, ' <h2>hello</h2>')