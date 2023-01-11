import random


class Property:
    def __init__(self):
        self._owner = ""
        self.sale_price = random.uniform(100.0, 3000.0)
        self.rent_price = random.uniform(1.0, 150.0)

    def is_available_for_sale(self):
        return not self._owner

    def get_owner(self):
        return self._owner

    def set_owner(self, new_owner):
        self._owner = new_owner

    def remove_owner(self):
        self._owner = ""

    def print_property(self):
        print(f"PRICE: {self.sale_price}, RENT: {self.rent_price}, OWNER: {self._owner}")
