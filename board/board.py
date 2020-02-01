'''
For adaption to a different coordinate system later, make a function to flip some input coordinate
system to the coordinate system used in this program --- in case you forget :)

TODO:
    Implement Kings

'''

class Board:

    def __init__(self):
        self._checker_positions = self.initial_piece_placement()
        self._hidden_board = None
        self.location_map = self.generate_location_map()

    def __repr__(self):
        return 'A board object'

    def initial_piece_placement(self, reset=False):
        if not reset:
            # return [
            #     ['x', 'b', 'x', 'x', 'x', 'w', 'x', 'w'],
            #     ['b', 'x', 'b', 'x', 'x', 'x', 'w', 'x'],
            #     ['x', 'b', 'x', 'x', 'x', 'w', 'x', 'w'],
            #     ['b', 'x', 'b', 'x', 'x', 'x', 'w', 'x'],
            #     ['x', 'b', 'x', 'x', 'x', 'w', 'x', 'w'],
            #     ['b', 'x', 'b', 'x', 'x', 'x', 'w', 'x'],
            #     ['x', 'b', 'x', 'x', 'x', 'w', 'x', 'w'],
            #     ['b', 'x', 'b', 'x', 'x', 'x', 'w', 'x'],
            # ]
            # return [
            #     ['x', 'b', 'x', 'x', 'x', 'w', 'x', 'w'],
            #     ['x', 'x', 'b', 'x', 'x', 'x', 'w', 'x'],
            #     ['x', 'b', 'x', 'x', 'x', 'w', 'x', 'w'],
            #     ['b', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            #     ['x', 'b', 'x', 'b', 'x', 'W', 'x', 'w'],
            #     ['b', 'x', 'b', 'x', 'x', 'x', 'x', 'x'],
            #     ['x', 'b', 'x', 'x', 'x', 'b', 'x', 'w'],
            #     ['b', 'x', 'b', 'x', 'x', 'x', 'w', 'x'],
            # ]
            return [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                    ['x', 'x', 'b', 'x', 'b', 'x', 'x', 'x'],
                    ['x', 'x', 'x', 'W', 'x', 'x', 'x', 'x'],
                    ['x', 'x', 'b', 'x', 'b', 'x', 'x', 'x'],
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
                ]

    def generate_location_map(self):
        location_map = {}
        k = 0
        for i in range(8):
            for j in range(8):
                location_map[k] = [i, j]
                k = k + 1
        return location_map

    def draw_board(self):
        print('  0   1   2   3   4   5   6   7')
        for i in range(8):
            print('+---+---+---+---+---+---+---+---+')
            print('| {} | {} | {} | {} | {} | {} | {} | {} | {}'.format(
                self.draw_peice(self.get_piece_from_location(0, i)),
                self.draw_peice(self.get_piece_from_location(1, i)),
                self.draw_peice(self.get_piece_from_location(2, i)),
                self.draw_peice(self.get_piece_from_location(3, i)),
                self.draw_peice(self.get_piece_from_location(4, i)),
                self.draw_peice(self.get_piece_from_location(5, i)),
                self.draw_peice(self.get_piece_from_location(6, i)),
                self.draw_peice(self.get_piece_from_location(7, i)),
                i
            ))
        print('+---+---+---+---+---+---+---+---+  ')

    def flip_coordinates(self, x, y):
        return y, x

    def get_piece_from_location(self, x, y):
        return self._checker_positions[x][y]

    def draw_peice(self, piece):
        if piece == 'x':
            return ' '
        return piece

    def get_opposite_piece(self, piece):
        if piece.lower() == 'b':
            return 'w'
        if piece.lower() == 'w':
            return 'b'
        return 'x'

    def location_is_on_board(self, x, y):
        if -1 < x < 8 and -1 < y < 8:
            return True
        return False

    def get_all_white_moves(self):
        moves = []
        jumps = []
        for i in range(8):
            for j in range(8):
                if self.get_piece_from_location(j, i).lower() == 'w':
                    if self.get_piece_from_location(j, i) == 'W':
                        if not jumps:
                            moves = moves + self.can_move_down(j, i)
                        jumps = jumps + self.can_attack_down(j, i)
                    if not jumps:
                        moves = moves + self.can_move_up(j, i)
                    jumps = jumps + self.can_attack_up(j, i)
        if jumps:
            terminating_jumps = []
            while jumps:
                jump = jumps.pop(0)
                if self.can_attack_up(jump[0], jump[1], 'w'):
                    for new_jump in self.can_attack_up(jump[0], jump[1], 'w'):
                        jumps.append(new_jump)
                else:
                    terminating_jumps.append(jump)
            return terminating_jumps
        else:
            return moves

    def get_all_black_moves(self):
        moves = []
        jumps = []
        for i in range(8):
            for j in range(8):
                if self.get_piece_from_location(j, i).lower() == 'b':
                    if not jumps:
                        moves = moves + self.can_move_down(j, i)
                    jumps = jumps + self.can_attack_down(j, i)
        if jumps:
            terminating_jumps = []
            while jumps:
                jump = jumps.pop(0)
                if self.can_attack_down(jump[0], jump[1], 'b'):
                    for new_jump in self.can_attack_down(jump[0], jump[1], 'b'):
                        jumps.append(new_jump)
                else:
                    terminating_jumps.append(jump)
            return terminating_jumps
        else:
            return moves

    def can_move_up(self, x, y):
        moves = []
        if self.location_is_on_board(x - 1, y - 1) and self.get_piece_from_location(x - 1, y - 1) == 'x':
            moves.append([x - 1, y - 1])
        if self.location_is_on_board(x + 1, y - 1) and self.get_piece_from_location(x + 1, y - 1) == 'x':
            moves.append([x + 1, y - 1])
        return moves

    def can_move_down(self, x, y):
        moves = []
        if self.location_is_on_board(x - 1, y + 1) and self.get_piece_from_location(x - 1, y + 1) == 'x':
            moves.append([x - 1, y + 1])
        if self.location_is_on_board(x + 1, y + 1) and self.get_piece_from_location(x + 1, y + 1) == 'x':
            moves.append([x + 1, y + 1])
        return moves

    def can_attack_up(self, x, y, phantom_piece=None):
        jumps = []
        if phantom_piece:
            piece_at_x_y = phantom_piece
        else:
            piece_at_x_y = self.get_piece_from_location(x, y)
        opposite_piece = self.get_opposite_piece(piece_at_x_y)
        if self.location_is_on_board(x - 1, y - 1) and self.get_piece_from_location(x - 1, y - 1).lower() == opposite_piece:
            if self.location_is_on_board(x - 2, y - 2) and [x - 2, y - 2] in self.can_move_up(x - 1, y - 1):
                jumps.append([x-2, y-2])
        if self.location_is_on_board(x + 1, y - 1) and self.get_piece_from_location(x + 1, y - 1).lower() == opposite_piece:
            if self.location_is_on_board(x + 2, y - 2) and [x + 2, y - 2] in self.can_move_up(x + 1, y - 1):
                jumps.append([x + 2, y - 2])
        return jumps

    def can_attack_down(self, x, y, phantom_piece=None):
        jumps = []
        if phantom_piece:
            piece_at_x_y = phantom_piece
        else:
            piece_at_x_y = self.get_piece_from_location(x, y)
        opposite_piece = self.get_opposite_piece(piece_at_x_y)
        if self.location_is_on_board(x - 1, y + 1) and self.get_piece_from_location(x - 1, y + 1).lower() == opposite_piece:
            if self.location_is_on_board(x - 2, y + 2) and [x - 2, y + 2] in self.can_move_down(x - 1, y + 1):
                jumps.append([x-2, y+2])
        if self.location_is_on_board(x + 1, y + 1) and self.get_piece_from_location(x + 1, y + 1).lower() == opposite_piece:
            if self.location_is_on_board(x + 2, y + 2) and [x + 2, y + 2] in self.can_move_down(x + 1, y + 1):
                jumps.append([x + 2, y + 2])
        return jumps







