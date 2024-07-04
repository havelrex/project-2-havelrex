# This program is for running unit tests for the LemonadeStand classes: LemonadeStand, InvalidSalesItemError, MenuItem
# Import all necessary classes for testing
import unittest
from LemonadeStand import InvalidSalesItemError, MenuItem, LemonadeStand


# This class using the unittest package provides a unit test framework. Subclassing TestCase and added methods that will help you test different input values and the corresponding results.
class TestLemonadeStand(unittest.TestCase):
    # This function sets up dictionary for day 0 and menu values in the objects
    def setUp(self):
        self.stand = LemonadeStand('Lemons R Us')
        self.item1 = MenuItem('lemonade', 0.5, 1.5)
        self.stand.add_menu_item(self.item1)
        self.item2 = MenuItem('cookie', 0.6, 0.8)
        self.stand.add_menu_item(self.item2)
        self.item3 = MenuItem('cookie', 0.2, 1)
        self.stand.add_menu_item(self.item3)
        self.day0 = { 'lemonade': 5, 'cookie': 2}

    # Assert function for ensuring correct sales for the day
    def test_enter_sales_for_today(self):
        self.stand.enter_sales_for_today(self.day0)
        self.assertEqual(len(self.stand._sales_record), 1)

    # Assert function for ensuring sales item
    def test_invalid_sales_item(self):
        with self.assertRaises(InvalidSalesItemError):
            self.stand.enter_sales_for_today({'invalid_item': 3})

    # Assert function for ensuring correct total sales for the given menu item
    def test_total_sales_for_menu_item(self):
        self.stand.enter_sales_for_today(self.day0)
        self.assertEqual(self.stand.total_sales_for_menu_item('lemonade'), 5)

    # Assert function for ensuring correct total sales for the given menu item
    def test_total_profit_for_menu_item(self):
        self.stand.enter_sales_for_today(self.day0)
        self.assertEqual(self.stand.total_profit_for_menu_item('lemonade'), 5 * (1.5 - 0.5))

    # Assert function for ensuring correct total sales for the stand
    def test_total_profit_for_stand(self):
        self.stand.enter_sales_for_today(self.day0)
        self.assertEqual(self.stand.total_profit_for_stand(), 5 * (1.5 - 0.5) + 2 * (1 - 0.2))


# The following code is to make sure this test module executable in unittest
if __name__ == "__main__":
    unittest.main()