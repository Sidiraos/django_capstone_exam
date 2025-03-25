from django.test import TestCase
from LittleLemonAPI.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, 80)
        self.assertEqual(item.inventory, 100)