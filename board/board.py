'''
For adaption to a different coordinate system later, make a function to flip some input coordinate
system to the coordinate system used in this program --- in case you forget :)

TODO:
    Implement Kings

'''

class Board:

    def __init__(self):
        self._checker_positions = self.initial_piece_placement()

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
        else:
            self._checker_positions = self.initial_piece_placement(False)
            return None

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

    def can_move_up(self, x, y):
        piece_at_x_y = self.get_piece_from_location(x, y)
        if piece_at_x_y == 'x':
            return None
        left, right = self.get_piece_from_location(x-1, y+1), self.get_piece_from_location(x+1, y+1)
        if left == 'x' and right == 'x':
            return[[x-1, y+1], [x+1, y+1]]
        if left == 'x':
            return [[x-1, y+1]]
        if right == 'x':
            return [[x+1, y+1]]
        return None

    def can_move_down(self, x, y):
        piece_at_x_y = self.get_piece_from_location(x, y)
        if piece_at_x_y == 'x':
            return None
        left, right = self.get_piece_from_location(x-1, y+1), self.get_piece_from_location(x+1, y+1)
        if left == 'x' and right == 'x':
            return[[x-1, y-1], [x+1, y-1]]
        if left == 'x':
            return [[x-1, y-1]]
        if right == 'x':
            return [[x+1, y-1]]
        return None





