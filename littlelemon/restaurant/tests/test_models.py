from django.test import TestCase
from restaurant.models import MenuItem, Booking
from decimal import Decimal

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title='IceCream', price=80, inventory=100)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "IceCream:80")

    def test_get_menu_item(self) -> None:
        item = MenuItem.objects.get(id = self.item1.id)
        self.assertEqual(item.title, 'Honey')
        self.assertEqual(item.price, Decimal(13.00).quantize(Decimal("0.00")))
        self.assertEqual(item.inventory, 100)
