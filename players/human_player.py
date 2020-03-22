class Human_Player:

    def __init__(self, color):
        self.color = color

    @classmethod
    def take_turn(self):
        if self.color == 'white':
            possible_moves = self.game_board.get_all_white_moves()
        else:
            possible_moves = self.game_board.get_all_black_moves()
        print(f'{self.color}\'s Turn. Possible Moves:')
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
                if self.color == 'white':
                    possible_moves = self.game_board.check_for_white_additional_jump(possible_moves[move_selection][-1])
                else:
                    possible_moves = self.game_board.check_for_black_additional_jump(possible_moves[move_selection][-1])
                if possible_moves:
                    print('You must continue jumping.')
                    self.game_board.draw_board()
            else:
                break