from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import  status

from django.contrib.auth import get_user_model
from .models import CookieStand

from django.urls import reverse

class CountryTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass"
        )
        testuser2.save()

        test_country = CookieStand.objects.create(
            name="rake",
            author=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_country.save()


    def setUp(self):
        self.client.login(username='testuser1', password="pass")




    def test_countries_model(self):
        cookie_stands = CookieStand.objects.get(id=1)
        actual_author = str(cookie_stands.author)
        actual_name = str(cookie_stands.name)
        actual_description = str(cookie_stands.description)
        self.assertEqual(actual_author, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_country_list(self):
        url = reverse("country_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        countrys = response.data
        self.assertEqual(len(countrys), 1)


    def test_auth_required(self):
        self.client.logout()
        url = reverse("country_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_author_can_delete(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("country_detail", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
