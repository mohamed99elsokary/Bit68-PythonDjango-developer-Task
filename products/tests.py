import json

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from . import models


class AddProductTestCase(APITestCase):
    def setup(self):
        user = User.objects.create_user(
            username="username", password="password", email="testcase@example.com"
        )
        token = Token.objects.create(user=user)
        return token

    def test_add_product_with_all_correct(self):

        data = {
            "seller": self.setup(),
            "name": "product_name",
            "price": 20.5,
        }
        response = self.client.post("/api/products/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_product_with_invalid_token(self):

        data = {
            "seller": "asdasdasd",
            "name": "product_name",
            "price": 20.5,
        }
        response = self.client.post("/api/products/", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_product_with_empty_name(self):
        data = {
            "seller": "asdasdasd",
            "name": "",
            "price": 20.5,
        }
        response = self.client.post("/api/products/", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_product_with_empty_price(self):
        data = {
            "seller": "asdasdasd",
            "name": "product_name",
            "price": "",
        }
        response = self.client.post("/api/products/", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_product_with_empty_seller(self):
        data = {
            "seller": "",
            "name": "product_name",
            "price": 20.5,
        }
        response = self.client.post("/api/products/", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_product_with_null_name(self):
        data = {
            "seller": "asdasdasd",
            "price": 20.5,
        }
        response = self.client.post("/api/products/", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_product_with_null_price(self):
        data = {
            "seller": "asdasdasd",
            "name": "product_name",
        }
        response = self.client.post("/api/products/", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_product_with_null_seller(self):
        data = {
            "name": "product_name",
            "price": 20.5,
        }
        response = self.client.post("/api/products/", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_product_with_price_less_than0(self):
        data = {
            "seller": self.setup(),
            "name": "product_name",
            "price": -1,
        }
        response = self.client.post("/api/products/", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetProductTestCase(APITestCase):
    def setup(self):
        user = User.objects.create_user(
            username="username", password="password", email="testcase@example.com"
        )
        token = Token.objects.create(user=user)
        for i in range(15):
            models.Product.objects.create(seller=user, name="product_name", price=15)
        return token

    def test_get_products(self):
        response = self.client.get(
            f"/api/products/?seller={self.setup()}&order=ascending"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
