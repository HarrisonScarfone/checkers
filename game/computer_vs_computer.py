from players.random_choice_player import Random_Choice_Player
from game.board import Board


class Computer_vs_Computer:

    def __init__(self):
        self.game_board = Board()
        self.whos_turn_is_it = 'black'
        self.player_1 = Random_Choice_Player('white')
        self.player_2 = Random_Choice_Player('black')
        self.game_over = False

    def computer_player_turn(self, player):
        if player.color == 'white':
            possible_moves = self.game_board.get_all_white_moves()
        else:
            possible_moves = self.game_board.get_all_black_moves()
        while possible_moves:
            check_for_jumps = [move for move in possible_moves if len(move) > 2]
            if check_for_jumps:
                possible_moves = check_for_jumps
            move_selection = player.make_move(possible_moves)
            print(possible_moves)
            print(move_selection)
            self.game_board.make_move(move_selection)
            if len(move_selection) > 2:
                if player.color == 'white':
                    possible_moves = self.game_board.check_for_white_additional_jump(move_selection[-1])
                else:
                    possible_moves = self.game_board.check_for_black_additional_jump(move_selection[-1])
            else:
                break

    def run_game(self):
        moves = 0
        while not self.game_over and moves < 300:
            moves = moves + 1
            if self.whos_turn_is_it == 'black':
                if self.player_1.color == 'black':
                    self.computer_player_turn(self.player_1)
                else:
                    self.computer_player_turn(self.player_2)
                self.whos_turn_is_it = 'white'
            elif self.whos_turn_is_it == 'white':
                if self.player_1.color == 'white':
                    self.computer_player_turn(self.player_1)
                else:
                    self.computer_player_turn(self.player_2)
                self.whos_turn_is_it = 'black'
            self.game_over = self.game_board.has_someone_won()
            if self.game_over:
                print(self.game_over)
            if moves == 199:
                print('Random moves not completing game.')