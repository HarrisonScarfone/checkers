from board.board import Board

b = Board()
b.draw_board()

print(b.get_all_white_moves())

print(b.get_all_black_moves())