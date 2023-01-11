from random import randint


class Player:
    BOARD_SIZE = 20

    def __init__(self):
        self._balance = 300.0
        self.position = 0

    def increase_balance(self, amount):
        self._balance += amount

    def decrease_balance(self, amount):
        self._balance -= amount

    def get_balance(self):
        return self._balance

    def is_balance_negative(self):
        return self._balance < 0

    def move(self):
        dice_number = randint(1, 6)
        if (self.position + dice_number) > (self.BOARD_SIZE - 1):
            self.position = (self.position + dice_number) - self.BOARD_SIZE
            self.increase_balance(100)
        else:
            self.position += dice_number
        return self.position


class PlayerImpulsive(Player):
    behavior = 'Impulsivo'

    def can_buy(self, property):
        return self._balance >= property.sale_price


class PlayerDemanding(Player):
    behavior = 'Exigente'

    def can_buy(self, property):
        if self._balance >= property.sale_price:
            return property.rent_price > 50.0
        return False


class PlayerCautious(Player):
    behavior = 'Cauteloso'

    def can_buy(self, property):
        return (self._balance - property.sale_price) >= 80.0


class PlayerRandom(Player):
    behavior = 'Aleatorio'

    def can_buy(self, property):
        if self._balance >= property.sale_price:
            return True if randint(0, 1) == 1 else False
        return False
