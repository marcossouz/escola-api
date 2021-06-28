from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse


class ViewTestCase(APITestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.test_user = User.objects.create_user("test_user","test@test.com" , "123456")
        self.client = APIClient()
        self.client.force_authenticate(user=self.test_user)
        
    
    def test_api_can_get_list_student(self):
        """Test API has ability to list students."""
        response = self.client.get(reverse('alunos-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         'Expected Response Code 200, received {0} instead.'.format(response.status_code))


    def test_api_can_create_a_student(self):
        """Test the api has student creation capability."""
        self.student_data = {"nome": "UserTest", "rg": "123456789", "cpf": "12345678910", "data_nascimento": "2018-03-02"}
        response = self.client.post(
            reverse('alunos-list'),
            self.student_data,
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, 
                        'Expected Response Code 201, received {0} instead.'.format(response.status_code))

