from game.board import Board
from players.random_choice_player import Random_Choice_Player
from players.human_player import Human_Player


class Human_Vs_Computer:

    def __init__(self, human_color, computer_color):
        self.game_board = Board()
        self.whos_turn_is_it = 'black'
        self.game_over = None
        self.computer_player = Random_Choice_Player(computer_color)
        self.human_player = Human_Player(human_color)

    def human_player_turn(self):
        if self.human_player.color == 'white':
            possible_moves = self.game_board.get_all_white_moves()
        else:
            possible_moves = self.game_board.get_all_black_moves()
        print('Players Turn. Possible Moves:')
        while possible_moves:
            check_for_jumps = [move for move in possible_moves if len(move) > 2]
            if check_for_jumps:
                possible_moves = check_for_jumps
            for index, move in enumerate(possible_moves):
                print(f'{index}: {self.game_board.get_human_readable_move_path(move)}')
            move_selection = None
            while move_selection is None:
                try:
                    move_selection = int(input('Enter choice: '))
                    self.game_board.make_move(possible_moves[move_selection])
                except ValueError:
                    print('Invalid entry.')
                except IndexError:
                    print('Invalid selection.')
            if len(possible_moves[move_selection]) > 2:
                if self.human_player.color == 'white':
                    possible_moves = self.game_board.check_for_white_additional_jump(possible_moves[move_selection][-1])
                else:
                    possible_moves = self.game_board.check_for_black_additional_jump(possible_moves[move_selection][-1])
                if possible_moves:
                    print('You must continue jumping.')
                    self.game_board.draw_board()
            else:
                break

    def computer_player_turn(self):
        if self.computer_player.color == 'white':
            possible_moves = self.game_board.get_all_white_moves()
        else:
            possible_moves = self.game_board.get_all_black_moves()
        while possible_moves:
            check_for_jumps = [move for move in possible_moves if len(move) > 2]
            if check_for_jumps:
                possible_moves = check_for_jumps
            move_selection = self.computer_player.make_move(possible_moves)
            self.game_board.make_move(possible_moves[move_selection])
            if len(possible_moves[move_selection]) > 2:
                if self.computer_player.color == 'white':
                    possible_moves = self.game_board.check_for_white_additional_jump(possible_moves[move_selection][-1])
                else:
                    possible_moves = self.game_board.check_for_black_additional_jump(possible_moves[move_selection][-1])
                if possible_moves:
                    print('You must continue jumping.')
                    self.game_board.draw_board()

    def run_game(self):
        while not self.game_over:
            self.game_board.draw_board()
            if self.whos_turn_is_it == 'black':
                if self.computer_player.color == 'black':
                    self.computer_player_turn()
                else:
                    self.human_player_turn()
                self.whos_turn_is_it = 'white'
            elif self.whos_turn_is_it == 'white':
                if self.computer_player.color == 'white':
                    self.computer_player_turn()
                else:
                    self.human_player_turn()
                self.whos_turn_is_it = 'black'
            self.game_over = self.game_board.has_someone_won()
            if self.game_over:
                print(self.game_over)


