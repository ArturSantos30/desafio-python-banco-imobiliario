import random


class Property:
    def __init__(self):
        self._owner = ""
        self.sale_price = random.uniform(1.0, 300.0)
        self.rent_price = random.uniform(1.0, 150.0)

    def is_available_to_sale(self):
        return not self._owner

    def get_owner(self):
        return self._owner

    def set_owner(self, new_owner):
        self._owner = new_owner

    def remove_owner(self):
        self._owner = ""

    def print_property(self):
        print(f"PRICE: {self.sale_price}, RENT: {self.rent_price}, OWNER: {self._owner}")


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
        dice_number = random.randint(1, 6)
        if (self.position + dice_number) > (self.BOARD_SIZE - 1):
            self.position = (self.position + dice_number) - self.BOARD_SIZE
            self.increase_balance(100)
        else:
            self.position += dice_number
        return self.position


class PlayerImpulsive(Player):
    id = 'Impulsive'

    def can_buy(self, property):
        return self._balance >= property.sale_price


class PlayerDemanding(Player):
    id = 'Demanding'

    def can_buy(self, property):
        if self._balance >= property.sale_price:
            return property.rent_price > 50.0
        return False


class PlayerCautious(Player):
    id = 'Cautious'

    def can_buy(self, property):
        return (self._balance - property.sale_price) >= 80.0


class PlayerRandom(Player):
    id = 'Random'

    def can_buy(self, property):
        if self._balance >= property.sale_price:
            return True if random.randint(0, 1) == 1 else False
        return False


class BoardGame:
    def __init__(self):
        self.BOARD_SIZE = 20
        self.turn = 0
        self.board = [Property() for i in range(self.BOARD_SIZE)]
        self.players = [PlayerImpulsive(), PlayerDemanding(), PlayerCautious(), PlayerRandom()]
        random.shuffle(self.players)

    def _remove_properties_from_player(self, competitor):
        for property in self.board:
            if property.get_owner() == competitor.id:
                property.remove_owner()

    def _get_player_index_by_id(self, id):
        for i in range(len(self.players)):
            if self.players[i].id == id:
                return i

    def start_turn(self, competitor):
        index_destination = competitor.move()
        property = self.board[index_destination]
        if property.is_available_to_sale():
            if competitor.can_buy(property):
                competitor.decrease_balance(property.sale_price)
                property.set_owner(competitor.id)
        else:
            competitor.decrease_balance(property.rent_price)
            if competitor.is_balance_negative():
                self._remove_properties_from_player(competitor)

    def remove_players_with_negative_balance(self):
        for competitor in self.players:
            if competitor.is_balance_negative():
                ind = self._get_player_index_by_id(competitor.id)
                self.players.pop(ind)

    def print_players(self):
        print("Players: [ ", end="")
        for p in self.players:
            print(f"{p.id} ", end="")
        print("]\n")

    def print_property(self):
        for p in self.board:
            print(p.print_property())

    def update_turn(self):
        self.turn += 1

    def get_player_id_with_highest_balance(self):
        id, balance = self.players[0].id, self.players[0].get_balance()
        for i in range(1, len(self.players)):
            if self.players[i].get_balance() > balance:
                balance = self.players[i].get_balance()
                id = self.players[i].id
        return id


def get_victory_percentage(statistics, total_games):
    for players, victories in statistics.items():
        print(f"{players}: {(victories * 100) / total_games}")


def get_biggest_winner(statistics):
    biggest_win = max(statistics.values())
    for key in statistics.keys():
        if statistics[key] == biggest_win:
            return key


SIMULATIONS = 300
LAST_ROUND = 1000
time_out_count = 0
sum_turns = 0
victories = {'Impulsive': 0, 'Demanding': 0, 'Cautious': 0, 'Random': 0}

for i in range(SIMULATIONS):
    game = BoardGame()
    while True:
        if game.turn == LAST_ROUND:
            time_out_count += 1
            player_id = game.get_player_id_with_highest_balance()
            victories[player_id] += 1
            break
        elif len(game.players) == 1:
            victories[game.players[0].id] += 1
            break
        else:
            game.update_turn()
            for competitor in game.players:
                game.start_turn(competitor)
            game.remove_players_with_negative_balance()
    sum_turns += game.turn
    del game

print("FIM DE JOGO")
print(f"{time_out_count} partidas terminaram por time out.")
print(f"As partidas demoraram em media {sum_turns / SIMULATIONS} turnos.")
print("A porcentagem de vitórias dos jogadores são:")
get_victory_percentage(victories, SIMULATIONS)
print(f"O comportamento que mais vence e o {get_biggest_winner(victories)}")
