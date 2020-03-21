'''
For adaption to a different coordinate system later, make a function to flip some input coordinate
system to the coordinate system used in this program --- in case you forget :)
'''


class Move_List_Node():
    def __init__(self, x, y, next_node=None):
        self.x = x
        self.y = y
        self.next_node = next_node

class Board:

    def __init__(self):
        self._checker_positions = self.initial_piece_placement()
        self.up_right = 'up_right'
        self.up_left = 'up_left'
        self.down_left = 'down_left'
        self.down_right = 'down_right'

    def __repr__(self):
        return 'A board object'

    def initial_piece_placement(self, reset=False):
        return [
            'x', 'b', 'x', 'b', 'x', 'b', 'x', 'b',
            'b', 'x', 'b', 'x', 'b', 'x', 'b', 'x',
            'x', 'b', 'x', 'b', 'x', 'b', 'x', 'b',
            'w', 'x', 'w', 'x', 'x', 'x', 'x', 'x',
            'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x',
            'w', 'x', 'w', 'x', 'w', 'x', 'w', 'x',
            'x', 'w', 'x', 'w', 'x', 'w', 'x', 'w',
            'w', 'x', 'w', 'x', 'w', 'x', 'w', 'x',
        ]


    def index_to_x_y(self, index):
        return index / 8, index % 8

    def x_y_to_index(self, x, y):
        return x + y * 8

    def get_piece_from_index(self, index):
        return self._checker_positions[index]

    def draw_piece(self, index):
        piece = self.get_piece_from_index(index)
        if piece == 'x':
            return ' '
        return piece

    def draw_board(self):
        print('    0   1   2   3   4   5   6   7', end='')
        for index, piece in enumerate(self._checker_positions):
            if index % 8 == 0:
                print('\n  ---------------------------------')
                print(f'{index // 8} |', end='')
            print(f' {piece} |', end='')
        print('\n   ---------------------------------')

    def draw_board_with_index_no_pieces(self):
        print('    0    1    2    3    4    5    6    7', end='')
        for index, piece in enumerate(self._checker_positions):
            if index % 8 == 0:
                print('\n  -----------------------------------------')
                print(f'{index // 8} |', end='')
            print(f' {index:02d} |', end='')
        print('\n  -----------------------------------------')

    def change_piece_at_index(self, index, change_to):
        self._checker_positions[index] = change_to

    def up_right_is_valid(self, index):
        return index > 8 and (index + 1) % 8 != 0

    def get_up_right_piece(self, index):
        if self.up_right_is_valid(index):
            return self.get_piece_from_index(index - 7)

    def up_left_is_valid(self, index):
        return index > 7 and index % 8 != 0

    def get_up_left_piece(self, index):
        if self.up_left_is_valid(index):
            return self.get_piece_from_index(index - 9)

    def down_right_is_valid(self, index):
        return index < 56 and (index + 1) % 8 != 0

    def get_down_right_piece(self, index):
        if self.down_right_is_valid(index):
            return self.get_piece_from_index(index + 9)

    def down_left_is_valid(self, index):
        return index < 56 and index % 8 != 0

    def get_down_left_piece(self, index):
        if self.down_left_is_valid(index):
            return self.get_piece_from_index(index + 7)

    def get_all_white_moves(self):

        moves = []

        for index, piece in enumerate(self._checker_positions):
            if piece.lower() == 'w':
                isKing = self.get_piece_from_index(index).isupper()
                up_left = self.get_up_left_piece(index)
                up_right = self.get_up_right_piece(index)
                if up_left:
                    if up_left == 'x':
                        moves.append((index, index - 9))
                    if up_left.lower() == 'b':
                        jump_to_square = self.get_up_left_piece(index - 9)
                        if jump_to_square:
                            moves.append((index, index - 9, index - 18))
                if up_right:
                    if up_right == 'x':
                        moves.append((index, index - 7))
                    if up_right.lower() == 'b':
                        jump_to_square = self.get_up_right_piece(index - 7)
                        if jump_to_square and jump_to_square == 'x':
                            moves.append((index, index - 7, index - 14))
                if isKing:
                    down_left = self.get_down_left_piece(index)
                    down_right = self.get_down_right_piece(index)
                    if down_left:
                        if down_left == 'x':
                            moves.append((index, index + 7))
                        if down_left.lower() == 'b':
                            jump_to_square = self.get_down_left_piece(index + 7)
                            if jump_to_square and jump_to_square == 'x':
                                moves.append((index, index + 7, index + 14))
                    if down_right:
                        if down_right == 'x':
                            moves.append((index, index + 9))
                        if down_right.lower() == 'b':
                            jump_to_square = self.get_down_right_piece(index + 9)
                            if jump_to_square and jump_to_square == 'x':
                                moves.append((index, index + 9, index + 18))
        return moves

    def get_all_black_moves(self):

        moves = []

        for index, piece in enumerate(self._checker_positions):
            if piece.lower() == 'b':
                isKing = self.get_piece_from_index(index).isupper()
                down_left = self.get_down_left_piece(index)
                down_right = self.get_down_right_piece(index)
                if down_left:
                    if down_left == 'x':
                        moves.append((index, index + 7))
                    if down_left.lower() == 'w':
                        jump_to_square = self.get_down_left_piece(index + 7)
                        if jump_to_square and jump_to_square == 'x':
                            moves.append((index, index + 7, index + 14))
                if down_right:
                    if down_right == 'x':
                        moves.append((index, index + 9))
                    if down_right.lower() == 'w':
                        jump_to_square = self.get_down_right_piece(index + 9)
                        if jump_to_square and jump_to_square == 'x':
                            moves.append((index, index + 9, index + 18))
                if isKing:
                    up_left = self.get_up_left_piece(index)
                    up_right = self.get_up_right_piece(index)
                    if up_left:
                        if up_left == 'x':
                            moves.append((index, index - 9))
                        if up_left.lower() == 'w':
                            jump_to_square = self.get_up_left_piece(index - 9)
                            if jump_to_square and jump_to_square == 'x':
                                moves.append((index, index - 9, index - 18))
                    if up_right:
                        if up_right == 'x':
                            moves.append((index, index - 7))
                        if up_right.lower() == 'w':
                            jump_to_square = self.get_up_right_piece(index - 7)
                            if jump_to_square and jump_to_square == 'x':
                                moves.append((index, index - 7, index - 14))
        return moves

    def get_black_move_from_index(self, index):

        moves = []

        isKing = self.get_piece_from_index(index).isupper()
        down_left = self.get_down_left_piece(index)
        down_right = self.get_down_right_piece(index)
        if down_left:
            if down_left == 'x':
                moves.append((index, index + 7))
            if down_left.lower() == 'w':
                jump_to_square = self.get_down_left_piece(index + 7)
                if jump_to_square and jump_to_square == 'x':
                    moves.append((index, index + 7, index + 14))
        if down_right:
            if down_right == 'x':
                moves.append((index, index + 9))
            if down_right.lower() == 'w':
                jump_to_square = self.get_down_right_piece(index + 9)
                if jump_to_square and jump_to_square == 'x':
                    moves.append((index, index + 9, index + 18))
        if isKing:
            up_left = self.get_up_left_piece(index)
            up_right = self.get_up_right_piece(index)
            if up_left:
                if up_left == 'x':
                    moves.append((index, index - 9))
                if up_left.lower() == 'w':
                    jump_to_square = self.get_up_left_piece(index - 9)
                    if jump_to_square and jump_to_square == 'x':
                        moves.append((index, index - 9, index - 18))
            if up_right:
                if up_right == 'x':
                    moves.append((index, index - 7))
                if up_right.lower() == 'w':
                    jump_to_square = self.get_up_right_piece(index - 7)
                    if jump_to_square and jump_to_square == 'x':
                        moves.append((index, index - 7, index - 14))
        return moves

    def get_white_moves_from_index(self, index):

        moves = []

        isKing = self.get_piece_from_index(index).isupper()
        up_left = self.get_up_left_piece(index)
        up_right = self.get_up_right_piece(index)
        if up_left:
            if up_left == 'x':
                moves.append((index, index - 9))
            if up_left.lower() == 'b':
                jump_to_square = self.get_up_left_piece(index - 9)
                if jump_to_square:
                    moves.append((index, index - 9, index - 18))
        if up_right:
            if up_right == 'x':
                moves.append((index, index - 7))
            if up_right.lower() == 'b':
                jump_to_square = self.get_up_right_piece(index - 7)
                if jump_to_square and jump_to_square == 'x':
                    moves.append((index, index - 7, index - 14))
        if isKing:
            down_left = self.get_down_left_piece(index)
            down_right = self.get_down_right_piece(index)
            if down_left:
                if down_left == 'x':
                    moves.append((index, index + 7))
                if down_left.lower() == 'b':
                    jump_to_square = self.get_down_left_piece(index + 7)
                    if jump_to_square and jump_to_square == 'x':
                        moves.append((index, index + 7, index + 14))
            if down_right:
                if down_right == 'x':
                    moves.append((index, index + 9))
                if down_right.lower() == 'b':
                    jump_to_square = self.get_down_right_piece(index + 9)
                    if jump_to_square and jump_to_square == 'x':
                        moves.append((index, index + 9, index + 18))
        return moves

    # this assumes that it is getting a valid move
    def make_move(self, move_path):
        self.change_piece_at_index(move_path[-1], self.get_piece_from_index(move_path[0]))
        for move_location in move_path[:-1]:
            self.change_piece_at_index(move_location, 'x')

    def get_human_readable_move_path(self, move_path):
        return [(index % 8, index // 8) for index in move_path]
