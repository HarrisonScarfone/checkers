'''
For adaption to a different coordinate system later, make a function to flip some input coordinate
system to the coordinate system used in this program --- in case you forget :)
'''

class Board:

    def __init__(self):
        self._checker_positions = self.initial_piece_placement()
        self._hidden_board = None
        self.location_map, self.reverse_location_map = self.generate_location_maps()

    def __repr__(self):
        return 'A board object'

    def initial_piece_placement(self, reset=False):
        if not reset:
            return [
                ['x', 'b', 'x', 'x', 'x', 'w', 'x', 'w'],
                ['b', 'x', 'b', 'x', 'x', 'x', 'w', 'x'],
                ['x', 'b', 'x', 'x', 'x', 'w', 'x', 'w'],
                ['b', 'x', 'b', 'x', 'x', 'x', 'w', 'x'],
                ['x', 'b', 'x', 'x', 'x', 'w', 'x', 'w'],
                ['b', 'x', 'b', 'x', 'x', 'x', 'w', 'x'],
                ['x', 'b', 'x', 'x', 'x', 'w', 'x', 'w'],
                ['b', 'x', 'b', 'x', 'x', 'x', 'w', 'x'],
            ]
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
            # return [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            #         ['x', 'x', 'x', 'x', 'x', 'x', 'b', 'x'],
            #         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            #         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            #         ['x', 'x', 'x', 'W', 'x', 'x', 'x', 'x'],
            #         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            #         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            #         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
            #     ]

    def generate_location_maps(self):
        location_map = {}
        reverse_location_map = {}
        k = 0
        for i in range(8):
            for j in range(8):
                location_map[k] = [j, i]
                reverse_location_map['{}{}'.format(j, i)] = k
                k = k + 1
        return location_map, reverse_location_map

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

    def draw_locations(self):
        for i in range(8):
            print('+-----+-----+-----+-----+-----+-----+-----+-----+')
            print('|  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |'.format(
                self.reverse_location_map['{}{}'.format(0, i)],
                self.reverse_location_map['{}{}'.format(1, i)],
                self.reverse_location_map['{}{}'.format(2, i)],
                self.reverse_location_map['{}{}'.format(3, i)],
                self.reverse_location_map['{}{}'.format(4, i)],
                self.reverse_location_map['{}{}'.format(5, i)],
                self.reverse_location_map['{}{}'.format(6, i)],
                self.reverse_location_map['{}{}'.format(7, i)],
            ))
        print('+---+---+---+---+---+---+---+---+')

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
                jumps.append([x-2, y-2, self.reverse_location_map['{}{}'.format(x, y)]])
        if self.location_is_on_board(x + 1, y - 1) and self.get_piece_from_location(x + 1, y - 1).lower() == opposite_piece:
            if self.location_is_on_board(x + 2, y - 2) and [x + 2, y - 2] in self.can_move_up(x + 1, y - 1):
                jumps.append([x + 2, y - 2, self.reverse_location_map['{}{}'.format(x, y)]])
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
                jumps.append([x-2, y+2, self.reverse_location_map['{}{}'.format(x, y)]])
        if self.location_is_on_board(x + 1, y + 1) and self.get_piece_from_location(x + 1, y + 1).lower() == opposite_piece:
            if self.location_is_on_board(x + 2, y + 2) and [x + 2, y + 2] in self.can_move_down(x + 1, y + 1):
                jumps.append([x + 2, y + 2, self.reverse_location_map['{}{}'.format(x, y)]])
        return jumps

    def get_all_moves_white(self):
        moves = {}
        jumps = []
        terminating_jumps = {}
        k = 0
        for i in range(8):
            for j in range(8):
                if self.get_piece_from_location(j, i).lower() == 'w':
                    if self.get_piece_from_location(j, i) == 'W':
                        if not jumps:
                            moves[k] = self.can_move_down(j, i)
                        jumps = jumps + self.can_attack_down(j, i)
                    else:
                        pass
                    if not jumps:
                        if k in moves:
                            moves[k] = moves[k] + self.can_move_up(j, i)
                        else:
                            moves[k] = self.can_move_up(j, i)
                    jumps = jumps + self.can_attack_up(j, i)
                k = k + 1
        if jumps:
            while jumps:
                jumps_to_add = []
                jump = jumps.pop(0)
                king_check = self.location_map[jump[2]]
                if self.get_piece_from_location(king_check[0], king_check[1]) == 'W' and self.can_attack_down(jump[0], jump[1], 'w'):
                    if len(jump) == 4 and jump[3] == 'down':
                        for new_jump in self.can_attack_down(jump[0], jump[1], 'w'):
                            jumps_to_add.append([new_jump[0], new_jump[1], jump[2], 'down'])
                    if len(jump) == 3:
                        for new_jump in self.can_attack_down(jump[0], jump[1], 'w'):
                            jumps_to_add.append([new_jump[0], new_jump[1], jump[2], 'down'])
                if self.can_attack_up(jump[0], jump[1], 'w'):
                    if len(jump) == 4 and jump[3] == 'up':
                        for new_jump in self.can_attack_up(jump[0], jump[1], 'w'):
                            jumps_to_add.append([new_jump[0], new_jump[1], jump[2], 'up'])
                    if len(jump) == 3:
                        for new_jump in self.can_attack_up(jump[0], jump[1], 'w'):
                            jumps_to_add.append([new_jump[0], new_jump[1], jump[2], 'up'])
                if not jumps_to_add:
                    if jump[2] in terminating_jumps:
                        terminating_jumps[jump[2]] = terminating_jumps[jump[2]] + [jump[0], jump[1]]
                    else:
                        terminating_jumps[jump[2]] = [jump[0], jump[1]]
                jumps = jumps + jumps_to_add
            return terminating_jumps
        else:
            return moves

    def get_all_moves_black(self):
        moves = {}
        jumps = []
        terminating_jumps = {}
        k = 0
        for i in range(8):
            for j in range(8):
                if self.get_piece_from_location(j, i).lower() == 'b':
                    if self.get_piece_from_location(j, i) == 'B':
                        if not jumps:
                            moves[k] = self.can_move_up(j, i)
                        jumps = jumps + self.can_attack_up(j, i)
                    else:
                        pass
                    if not jumps:
                        if k in moves:
                            moves[k] = moves[k] + self.can_move_down(j, i)
                        else:
                            moves[k] = self.can_move_down(j, i)
                    jumps = jumps + self.can_attack_down(j, i)
                k = k + 1
        if jumps:
            while jumps:
                jumps_to_add = []
                jump = jumps.pop(0)
                king_check = self.location_map[jump[2]]
                if self.get_piece_from_location(king_check[0], king_check[1]) == 'W' and self.can_attack_up(jump[0], jump[1], 'w'):
                    if len(jump) == 4 and jump[3] == 'up':
                        for new_jump in self.can_attack_up(jump[0], jump[1], 'b'):
                            jumps_to_add.append([new_jump[0], new_jump[1], jump[2], 'up'])
                    if len(jump) == 3:
                        for new_jump in self.can_attack_up(jump[0], jump[1], 'b'):
                            jumps_to_add.append([new_jump[0], new_jump[1], jump[2], 'up'])
                if self.can_attack_down(jump[0], jump[1], 'b'):
                    if len(jump) == 4 and jump[3] == 'down':
                        for new_jump in self.can_attack_down(jump[0], jump[1], 'b'):
                            jumps_to_add.append([new_jump[0], new_jump[1], jump[2], 'down'])
                    if len(jump) == 3:
                        for new_jump in self.can_attack_down(jump[0], jump[1], 'b'):
                            jumps_to_add.append([new_jump[0], new_jump[1], jump[2], 'down'])
                if not jumps_to_add:
                    if jump[2] in terminating_jumps:
                        terminating_jumps[jump[2]] = terminating_jumps[jump[2]] + [jump[0], jump[1]]
                    else:
                        terminating_jumps[jump[2]] = [jump[0], jump[1]]
                jumps = jumps + jumps_to_add
            return terminating_jumps
        else:
            return moves





