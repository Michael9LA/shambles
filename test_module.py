import unittest
from restaurant import Table


class UnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.table02 = Table(2)
        self.table05 = Table(5)
        self.table06 = Table(6)

    def test_order(self):
        self.table02.order('Food', 10.00, 3)
        actual = self.table02.bill
        expected = [{
            'item': 'Food',
            'price': 10.00,
            'quantity': 3}]
        self.assertEqual(
            actual, expected,
            "Expected `order` method to create object in bill instance variable."
        )

    def test_order_no_quantity(self):
        self.table02.order('Food', 10.00)
        actual = self.table02.bill
        expected = [{
            'item': 'Food',
            'price': 10.00,
            'quantity': 1}]
        self.assertEqual(
            actual, expected,
            "Expected calling `order` with no quantity to create item with quantity 1."
        )

    def test_remove(self):
        self.table02.order('Food', 10.00, 5)
        self.table02.remove('Food', 10.00, 3)
        actual = self.table02.bill
        expected = [{
            'item': 'Food',
            'price': 10.00,
            'quantity': 2}]
        self.assertEqual(
            actual, expected,
            "Expected `remove` method to reduce quantity of existing item."
        )

    def test_remove_no_item(self):
        self.table02.order('Food', 10.00, 1)
        result = self.table02.remove('Food', 11.00, 1)
        self.assertFalse(
            result,
            "Expected `remove` method with item and price not present in bill to return False."
        )
        result = self.table02.remove('Food2', 10.00, 1)
        self.assertFalse(
            result,
            "Expected `remove` method with item and price not present in bill to return False."
        )

    def test_get_subtotal(self):
        self.table02.order('Food1', 10.00, 3)
        self.table02.order('Food2', 20.00, 1)
        self.table02.order('Food3', 0.50, 1)
        actual = self.table02.get_subtotal()
        expected = 50.50
        self.assertAlmostEqual(
            actual, expected, 2,
            "Expected balance to 2 decimal places to be 50.50."
        )

    def test_get_total(self):
        self.table05.order('Food1', 10.00, 3)
        self.table05.order('Food2', 20.00, 1)
        self.table05.order('Food3', 0.60, 1)
        actual = self.table05.get_total(0.15)
        expected = {
            'Sub Total': '£50.60',
            'Service Charge': '£7.59',
            'Total': '£58.19'
        }
        self.assertEqual(
            actual, expected,
            "Expected different dictionary from `get_total`."
        )

    def test_split_bill(self):
        self.table06.order('Food1', 20.00, 3)
        self.table06.order('Food2', 10.00, 1)
        self.table06.order('Food3', 3.20, 1)
        actual = self.table06.split_bill()
        expected = 12.20
        self.assertAlmostEqual(
            actual, expected, 2,
            "Expected `split_bill` to return 12.20 to 2 decimal places."
        )


if __name__ == "__main__":
    unittest.main()
