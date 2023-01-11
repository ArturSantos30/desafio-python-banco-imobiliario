class GameStatistics:
    SIMULATIONS = 300

    def __init__(self):
        self.time_out_count = 0
        self.sum_turns = 0
        self.victories = {'Impulsivo': 0, 'Exigente': 0, 'Cauteloso': 0, 'Aleatorio': 0}

    def update_time_out_count(self):
        self.time_out_count += 1

    def update_sum_turns_count(self, shift):
        self.sum_turns += shift

    def add_player_victory(self, behavior):
        self.victories[behavior] += 1

    def _get_victory_percentage(self):
        for players, wins in self.victories.items():
            print(f"{players}: {((wins * 100) / self.SIMULATIONS):.2f}")

    def _get_winner(self):
        biggest_win = max(self.victories.values())
        for key in self.victories.keys():
            if self.victories[key] == biggest_win:
                return key

    def _get_matches_average(self):
        return self.sum_turns/self.SIMULATIONS

    def print_number_of_matches_ended_by_timeout(self):
        if self.time_out_count == 1:
            print("1 partida terminou por timeout")
        elif self.time_out_count == 0:
            print("Nenhuma partida terminou por timeout")
        else:
            print(f"{self.time_out_count} partidas terminaram por time out.")

    def print_matches_average(self):
        print(f"As partidas demoraram em media {self._get_matches_average():.2f} turnos.")

    def print_players_victory_percentage(self):
        print("A porcentagem de vitórias dos jogadores são:")
        self._get_victory_percentage()

    def print_winner(self):
        print(f"O comportamento que mais vence e o {self._get_winner()}")
