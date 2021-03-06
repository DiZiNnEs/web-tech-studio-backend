from django.test import TestCase
from django.urls import reverse


class IndexViewTestCase(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'main_app/index.html')


class ServicesViewViewTestCase(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/services/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('services'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('services'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'main_app/services.html')
