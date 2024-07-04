# The program is for recording the menu items and daily sales of a lemonade stand. Contains classes: MenuItem, SalesForDay, InvalidSalesItemError and LemonadeStand.
# All data members of each class marked as private (a leading underscore in the name).

# A MenuItem class represents a menu item to be offered for sale at the lemonade stand.
# init method - takes as parameters three values with which to initialize the MenuItem: its name, its wholesale cost, and its selling price
# get methods for each of the data members: get_name(), get_wholesale_cost(), and get_selling_price()
class MenuItem:
    """
    This class represents a menu item to be offered for sale at the lemonade stand.
    Attributes:
           _name (str): The name of the menu item.
           _wholesale_cost (float): The wholesale cost of the menu item.
           _selling_price (float): The selling price of the menu item.
    """

    def __init__(self, name, wholesale_cost, selling_price):
        """
        Initializes a new MenuItem instance.
        Parameters:
            name (str): The name of the menu item.
            wholesale_cost (float): The wholesale cost of the menu item.
            selling_price (float): The selling price of the menu item.
        """
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        """Gets the name of the menu item and returns the name of the menu item as a string."""
        return self._name

    def get_wholesale_cost(self):
        """Gets the wholesale cost of the menu item and returns the wholesale cost of the menu item as a float."""
        return self._wholesale_cost

    def get_selling_price(self):
        """Gets the selling price of the menu item and returns the selling price of the menu item as a float."""
        return self._selling_price


# A SalesForDay class represents the sales for a particular day.
# init method - takes as parameters two values with which to initialize the SalesForDay: the day (an integer for the number of days the stand has been open so far),
# and a dictionary whose keys are the names of the items sold, and whose values are the numbers of those items sold that day
# get methods for each of the data members: get_day() and get_sales_dict()
class SalesForDay:
    """
    Represents the sales for a particular day.
    Attributes:
    _day (int): The day number.
    _sales_dict (dict): A dictionary where keys are item names and values are the number of items sold.
    """

    def __init__(self, day, sales_dict):
        """Initializes a new SalesForDay instance.
            Parameters:
            day (int): The day number.
            sales_dict (dict): A dictionary of sales where keys are item names and values are quantities sold.
        """
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        """Gets the day number and returns the day number as an int"""
        return self._day

    def get_sales_dict(self):
        """Gets the dictionary of sales for the day and returns a dictionary of sales where keys are item names and
        values are quantities sold."""
        return self._sales_dict


# A LemonadeStand object represents a lemonade stand, which has four data members:
# a string for the name of the stand an integer representing the current day
# a dictionary of MenuItem objects, where the keys are the names of the items and the values are the corresponding MenuItem objects a list of SalesForDay objects
# init method - takes as a parameter the name of the stand; initializes the name to that value, initializes current day to zero, initializes the menu to an empty dictionary,
# and initializes the sales record to an empty list (remember to not use any mutable default arguments) a get method for the name: get_name()
# add_menu_item - takes as a parameter a MenuItem object and adds it to the menu dictionary
# enter_sales_for_today - takes as a parameter a dictionary where the keys are names of items sold and the corresponding values are how many of the item were sold.
# If the name of any item sold doesn't match the name of any MenuItem in the menu, it raises an InvalidSalesItemError (you'll need to define this exception class). Otherwise,
# it creates a new SalesForDay object, using the current day and the dictionary that was passed in, adds that object to the list of SalesForDay objects, and then increments the current day by 1
# get_sales_dict_for_day - takes as a parameter an integer representing a particular day, and returns the dictionary of sales for that day (not a SalesForDay object)
# total_sales_for_menu_item - takes as a parameter the name of a menu item and returns the total number of that item sold over the history of the stand
# total_profit_for_menu_item - takes as a parameter the name of a menu item and returns the total profit on that item over the history of the stand
# total_profit_for_stand - takes no parameters and returns the total profit on all items sold over the history of the stand
class LemonadeStand:
    """
    Represents a lemonade stand.
    Attributes:
        _name (str): The name of the lemonade stand.
        _current_day (int): The current day number.
        _sales_record (list): A list of SalesForDay objects.
        _menu (dict): A dictionary of MenuItem objects with item names as keys.
    """

    def __init__(self, name: str):
        """
        Initializes a new LemonadeStand instance.
        Parameters:
        name (str): The name of the lemonade stand.
        """
        self._name = name
        self._current_day = 0
        self._sales_record = []
        self._menu = {}  # dictionary to store menu items {name: MenuItem object}
        self._sales_dict = {}  # dictionary to store daily sales {day: {item_name: quantity}}
        self._wholesale_cost = []

    def get_name(self):
        """Gets the name of the menu item and returns the name of the menu item."""
        return self._name

    def add_menu_item(self, menu_item: MenuItem):
        """
        Adds a menu item to the lemonade stand's menu.
        Parameters:
        menu_item (MenuItem): The menu item to be added.
        """
        self._menu[menu_item.get_name()] = menu_item

    def enter_sales_for_today(self, sales_dict: dict):
        """
        Records the sales for the current day.

        Parameters:
        sales_dict (dict): A dictionary where keys are item names and values are quantities sold.

        Raises:
        InvalidSalesItemError: If an item in the sales dictionary is not on the menu.
        """

        for item in sales_dict.keys():
            if item not in self._menu:
                raise InvalidSalesItemError(f"Invalid item: {item} is not on the menu.")
        sales_for_day = SalesForDay(self._current_day, sales_dict)
        self._sales_record.append(sales_for_day)
        self._current_day += 1

    def sales_of_menu_item_for_day(self, day: int, item_name: str):
        """
        Gets the sales of a specific menu item for a particular day.

        Parameters:
        day (int): The day number.
        item_name (str): The name of the menu item.

        Returns:
        int: The number of items sold on that day.
        """

        if day < 0 or day >= len(self._sales_record):
            return 0
        sales_dict = self._sales_record[day].get_sales_dict()
        return sales_dict.get(item_name, 0)

    def total_sales_for_menu_item(self, item_name: str):
        """
        Gets the total sales of a specific menu item over the history of the stand.

        Parameters:
        item_name (str): The name of the menu item.

        Returns:
        int: The total number of items sold.
        """

        total_sales = 0
        for sales_for_day in self._sales_record:
            total_sales += sales_for_day.get_sales_dict().get(item_name, 0)
        return total_sales

    def total_profit_for_menu_item(self, item_name: str):
        """
        Gets the total profit of a specific menu item over the history of the stand.
        Parameters:
        item_name (str): The name of the menu item.

        Returns:
        float: The total profit made from the item.
        """

        menu_item = self._menu.get(item_name)
        if not menu_item:
            return 0
        total_sales = self.total_sales_for_menu_item(item_name)
        profit_per_item = menu_item.get_selling_price() - menu_item.get_wholesale_cost()
        return total_sales * profit_per_item

    def total_profit_for_stand(self):
        """
        Gets the total profit of the lemonade stand over its history.

        Returns:
        float: The total profit made from all items.
        """
        total_profit = 0
        for item_name in self._menu:
            total_profit += self.total_profit_for_menu_item(item_name)
        return total_profit


class InvalidSalesItemError(Exception):
    """This class handles invalid error condition."""
    pass

# Defining main function to run test
def main():
    """Main function to test lemonade stand."""
    print("Main function to test LemonadeStand")

# Initializing a new LemonadeStand and calling it 'Lemons R Us'
stand = LemonadeStand('Lemons R Us')

# Initializing lemonade as a menu item (wholesale cost is 50 cents, selling price is $1.50)
item1 = MenuItem('lemonade', 0.5, 1.5)
# Adding lemonade to the menu for 'Lemons R Us'
stand.add_menu_item(item1)

# Initializing nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
item2 = MenuItem('nori', 0.6, 0.8)
# Adding nori to the menu for 'Lemons R Us'
stand.add_menu_item(item2)

# Initializing cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
item3 = MenuItem('cookie', 0.2, 1)
# Adding cookies to the menu for 'Lemons R Us'
stand.add_menu_item(item3)

# This dictionary records that on day zero, 5 lemonades were sold, 2 cookies were sold, and no nori was sold
sales_for_day = {'lemonade': 5, 'cookie': 2}

#Below is sample of negative test that includes item that is not inside dictionary
#sales_for_day = {'lemonade': 5, 'cookie': 2, 'boori':7}

# Record the sales for day 0
stand.enter_sales_for_today(sales_for_day)

# print the total profit for lemonade stand
print(f"lemonade profit = {stand.total_profit_for_menu_item('lemonade')}")