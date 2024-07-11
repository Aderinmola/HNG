from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationTest(APITestCase):
    def test_user_registration(self):
        url = reverse('register')
        data = {
            "first_name": "test",
            "last_name": "user",
            "email": "testuser@example.com",
            "password": "testpassword123",
            "phone": "09016756453"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TokenGenerationTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            # username='testuser', 
            # email='testuser@example.com', 
            # password='testpassword123'

            first_name="test",
            last_name="user",
            email="testuser@example.com",
            password="testpassword123",
            phone="09016756453"
        )

    def test_token_generation(self):
        url = reverse('login')
        data = {
            "email": "testuser@example.com",
            "password": "testpassword123",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertIn('access', response.data)
        # self.assertIn('refresh', response.data)
