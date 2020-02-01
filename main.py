from board.board import Board

b = Board()
b.draw_board()

print(b.get_all_white_moves())
print(b.get_all_black_moves())

# print(b.can_attack_up(4,5))

# print(b.location_is_on_board(8,1))