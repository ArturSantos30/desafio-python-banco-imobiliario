from board_game import BoardGame
from game_statistics import GameStatistics

SIMULATIONS = 300
LAST_ROUND = 1000


def main():
    statistics = GameStatistics()

    for i in range(SIMULATIONS):
        game = BoardGame()
        while True:
            if game.turn == LAST_ROUND:
                statistics.update_time_out_count()
                player_behavior = game.get_player_behavior_with_highest_balance()
                statistics.add_player_victory(player_behavior)
                break
            elif len(game.players) == 1:
                statistics.add_player_victory(game.players[0].behavior)
                break
            else:
                game.update_turn()
                for competitor in game.players:
                    game.start_turn(competitor)
                game.remove_players_with_negative_balance()
        statistics.update_sum_turns_count(game.turn)
        del game

    print("FIM DE JOGO")
    statistics.print_number_of_matches_ended_by_timeout()
    statistics.print_matches_average()
    statistics.print_players_victory_percentage()
    statistics.print_winner()


if __name__ == "__main__":
    main()
