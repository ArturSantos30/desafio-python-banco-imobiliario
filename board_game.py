from property import Property
from player import *
import random


class BoardGame:
    def __init__(self):
        self.BOARD_SIZE = 20
        self.turn = 0
        self.board = [Property() for i in range(self.BOARD_SIZE)]
        self.players = [PlayerImpulsive(), PlayerDemanding(), PlayerCautious(), PlayerRandom()]
        random.shuffle(self.players)

    def _remove_properties_from_player(self, competitor):
        for property in self.board:
            if property.get_owner() == competitor.behavior:
                property.remove_owner()

    def _get_player_index_by_behavior(self, behavior):
        for i in range(len(self.players)):
            if self.players[i].behavior == behavior:
                return i

    def start_turn(self, competitor):
        index_destination = competitor.move()
        property = self.board[index_destination]
        if property.is_available_for_sale():
            if competitor.can_buy(property):
                competitor.decrease_balance(property.sale_price)
                property.set_owner(competitor.behavior)
        else:
            competitor.decrease_balance(property.rent_price)
            if competitor.is_balance_negative():
                self._remove_properties_from_player(competitor)

    def remove_players_with_negative_balance(self):
        for competitor in self.players:
            if competitor.is_balance_negative():
                ind = self._get_player_index_by_behavior(competitor.behavior)
                self.players.pop(ind)

    def print_players(self):
        print("Players: [ ", end="")
        for p in self.players:
            print(f"{p.behavior} ", end="")
        print("]\n")

    def print_property(self):
        for p in self.board:
            print(p.print_property())

    def update_turn(self):
        self.turn += 1

    def get_player_behavior_with_highest_balance(self):
        behavior, balance = self.players[0].behavior, self.players[0].get_balance()
        for i in range(1, len(self.players)):
            if self.players[i].get_balance() > balance:
                balance = self.players[i].get_balance()
                behavior = self.players[i].behavior
        return behavior
