import json

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class UserRegistrationTestCase(APITestCase):
    def test_correct_registration(self):
        data = {
            "username": "username",
            "email": "testcase@example.com",
            "password": "password",
        }
        response = self.client.post("/api/register", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_short_password_registration(self):
        data = {
            "username": "username",
            "email": "testcase@example.com",
            "password": "aw",
        }
        response = self.client.post("/api/register", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_empty_password_registration(self):
        data = {
            "username": "username",
            "email": "testcase@example.com",
            "password": "",
        }
        response = self.client.post("/api/register", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_null_password_registration(self):
        data = {"username": "username", "email": "testcase@example.com"}
        response = self.client.post("/api/register", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_empty_username_registration(self):
        data = {"username": "", "password": "password", "email": "testcase@example.com"}
        response = self.client.post("/api/register", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_null_username_registration(self):
        data = {"password": "password", "email": "testcase@example.com"}
        response = self.client.post("/api/register", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_empty_email_registration(self):
        data = {
            "username": "username",
            "password": "password",
            "email": "",
        }
        response = self.client.post("/api/register", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_null_email_registration(self):
        data = {
            "username": "username",
            "password": "password",
        }
        response = self.client.post("/api/register", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_email_registration(self):
        data = {
            "email": "email",
            "username": "username",
            "password": "password",
        }
        response = self.client.post("/api/register", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_taken_username_registration(self):
        # create user for exesting test case
        User.objects.create_user(
            username="username", password="password", email="testcase@example.com"
        )

        data = {
            "username": "username",
            "email": "testcase@example.com",
            "password": "password",
        }
        response = self.client.post("/api/register", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserLoginTestCase(APITestCase):
    def test_correct_login(self):
        User.objects.create_user(
            username="username", password="password", email="testcase@example.com"
        )
        data = {
            "username": "username",
            "email": "testcase@example.com",
            "password": "password",
        }
        response = self.client.post("/api/login", data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_password_incorrect(self):
        User.objects.create_user(
            username="username", password="password", email="testcase@example.com"
        )
        data = {
            "username": "username",
            "email": "testcase@example.com",
            "password": "passwordaa",
        }
        response = self.client.post("/api/login", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_empty_username(self):
        User.objects.create_user(
            username="username", password="password", email="testcase@example.com"
        )
        data = {
            "username": "",
            "email": "testcase@example.com",
            "password": "passwordaa",
        }
        response = self.client.post("/api/login", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_null_username(self):
        User.objects.create_user(
            username="username", password="password", email="testcase@example.com"
        )
        data = {
            "email": "testcase@example.com",
            "password": "passwordaa",
        }
        response = self.client.post("/api/login", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_empty_password(self):
        User.objects.create_user(
            username="username", password="password", email="testcase@example.com"
        )
        data = {
            "username": "username",
            "email": "testcase@example.com",
            "password": "",
        }
        response = self.client.post("/api/login", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_null_password(self):
        User.objects.create_user(
            username="username", password="password", email="testcase@example.com"
        )
        data = {
            "username": "username",
            "email": "testcase@example.com",
        }
        response = self.client.post("/api/login", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_username_not_registered(self):
        User.objects.create_user(
            username="username", password="password", email="testcase@example.com"
        )
        data = {
            "username": "usernameaa",
            "email": "testcase@example.com",
            "password": "passwordaa",
        }
        response = self.client.post("/api/login", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
