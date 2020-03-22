from game.board import Board

class Human_Vs_Human:

    def __init__(self):
        self.game_board = Board()
        self.whos_turn_is_it = 'black'
        self.game_over = None

    def white_turn(self):
        possible_moves = self.game_board.get_all_white_moves()
        print('Whites Turn. Possible Moves:')
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
                possible_moves = self.game_board.check_for_white_additional_jump(possible_moves[move_selection][-1])
                if possible_moves:
                    print('You must continue jumping.')
                    self.game_board.draw_board()
            else:
                break

    def black_turn(self):
        possible_moves = self.game_board.get_all_black_moves()
        print('Blacks Turn. Possible Moves:')
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
                possible_moves = self.game_board.check_for_black_additional_jump(possible_moves[move_selection][-1])
                if possible_moves:
                    print('You must continue jumping.')
                    self.game_board.draw_board()
            else:
                break

    def run_game(self):
        while not self.game_over:
            self.game_board.draw_board()
            if self.whos_turn_is_it == 'black':
                self.black_turn()
                self.whos_turn_is_it = 'white'
            elif self.whos_turn_is_it == 'white':
                self.white_turn()
                self.whos_turn_is_it = 'black'
            self.game_over = self.game_board.has_someone_won()
            if self.game_over:
                print(self.game_over)


