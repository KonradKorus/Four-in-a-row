import game_functions as gf

number_of_rows = int(input("Chose number of column (normal is 7): ")) 
number_of_columns = int(input("Chose number of column (normal is 6): "))
in_a_row = 4  #number of elements in a row, which cousing win

game_board = [[0 for i in range(number_of_rows)] for i in range(number_of_columns)]


#column_choice = 5 input("Pick a column: ")
#row_choice = 5 input("Pick a row: ")

    
#showing game board
print("   "+"  ".join([str(i) for i in range(number_of_rows)]))

for i, row in zip(range(number_of_columns), game_board):
    print(i, row)

