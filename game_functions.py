#function checks if current move (player_row, player_column) couses win for current player
def check_win(game_board, player,player_row, player_column, in_a_row):
    
    #function checks if line has in_a_row elemnts of the same type (1 or 2 [players]) 
    def check_line(line, win_type):
        #check if win is even possible in this turn                                                   
        if line.count(player) < in_a_row:                              
            return False

        #breaking line into pieces of in_a_row elements, then check count  
        for field in range(len(line[0:len(game_board)-in_a_row + 1])):  
            temp = line[field: field+in_a_row] 
            if temp.count(player) >= in_a_row:
                print(f"Player {player} won {win_type}. Congratulations !!!")    
                return True
        return False
    
   
    #======vertical========
    vertical = []
    for row in game_board:
        vertical.append(row[player_column])
    
    check_line(vertical, "vertically")


    #=====horizontal======
    horizontal = game_board[player_row]
    check_line(horizontal, "horizontally")


    #======diagonal====== (from left to right  \)
    diagonal=[]

    #set starting values based on user input
    if player_row-player_column > 0: 
        start_row = player_row-player_column
    else :
        start_row = 0

    if player_column-player_row > 0:
        start_column = player_column-player_row
    else :
        start_column = 0
    
  
    #adding matching item to diagonal  
    while start_row < len(game_board) and start_column < len(game_board[0]):
        diagonal.append(game_board[start_row][start_column])
        start_row+=1
        start_column+=1
    
    check_line(diagonal, "diagonally (left to right)")


    #=====diagonal_2===== (from right to left /)
    diagonal=[]
    
    #set starting values based on user input
    if player_column+player_row < len(game_board[0]):
        start_column = player_column+player_row
    else :
        start_column = len(game_board[0])-1
  
    if player_column + player_row < len(game_board):
        start_row=0
    else:
        start_row = player_column + player_row-len(game_board)
    

    #adding matching item to diagonal  
    while start_row < len(game_board) and start_column >= 0 :
        diagonal.append(game_board[start_row][start_column])
        start_row+=1
        start_column-=1
    
    check_line(diagonal, "diagonally (right to left)")

