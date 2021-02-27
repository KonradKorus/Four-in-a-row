board_size_x = 7
board_size_y = 6
in_a_row = 4

game = [[0 for i in range(board_size_x)] for i in range(board_size_y)]


column_choice = input("Pick a column: ")
row_choice = input("Pick a row: ")

#showing game board

print("   "+"  ".join([str(i) for i in range(board_size_x)]))

for i, row in zip(range(board_size_y), game):
    print(i, row)
