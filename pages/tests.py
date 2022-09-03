from django.urls import reverse
from django.test import TestCase


class HomePageTests(TestCase):
    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_url(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'HomePage')
        