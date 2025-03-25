from django.test import TestCase
from LittleLemonAPI.models import MenuItem
from django.contrib.auth.models import User


class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")  # Authentification
        self.menu = MenuItem.objects.create(title="IceCream", price=80, inventory=100)

    def test_get_all(self):
        response = self.client.get('/api/menu-items/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)