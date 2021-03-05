import game_functions as gf
import itertools

game_start = True

#loop for app running 
while game_start:

    number_of_rows = int(input("Choose numer of rows (basic is 7): "))
    number_of_columns = int(input("Choose numer of rows (basic is 6): "))
    in_a_row = 4  #number of elements in a row, which cousing win

    players= itertools.cycle([1,2])
    turn_count = 1

    game_end = False

    #generating game_board
    game = [[0 for i in range(number_of_rows)] for i in range(number_of_columns)]
    

    #loop for current_game
    while not game_end:
        current_player=next(players)
        print(f"\n=======Turn {turn_count} (Player {current_player})=======\n")
        gf.show_board(game)
        game, game_end = gf.make_move(game,current_player,in_a_row)
        if game_end:
            gf.show_board(game)

        turn_count+=1


    #defining play again or close app
    play_again=input("Do you want to play again (y/n):")

    #loop for wrong input
    while play_again!='n' and play_again != 'y':
        play_again=input("Wrong input pick between y/n:")
    
    if play_again.lower() == "y":
        print("restaring...")
        game_start=True
    else:
        print("Bye!")
        game_start=False



    