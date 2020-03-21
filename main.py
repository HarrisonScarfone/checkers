from board.board import Board

b = Board()

b.draw_board()
#
b.draw_board_with_index_no_pieces()
#
# moves = b.get_all_white_moves()
# bmoves = b.get_all_black_moves()
#
# print(moves)
# print(bmoves)
#
# b.make_move((40, 33, 26))
#
# b.draw_board()

c = b.get_black_move_from_index(17)
print(c)

print(b.get_human_readable_move_path((42,35,28)))

