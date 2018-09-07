from game import game
import sys
import os


gomoku = game()

gomoku.create_board()

os.system('cls' if os.name == 'nt' else 'clear')

while(1):

    #os.system('cls' if os.name == 'nt' else 'clear')
    
    while(1):

        print("Enter a x position:")
        human_x_input = sys.stdin.readline()
            
        print("Enter a y position:")
        human_y_input = sys.stdin.readline()
    
        if(gomoku.play_human(human_x_input,human_y_input) == True):
            break
            
        else:
            print("Jogue novamente, jogada proibida")
    
    while(1):
        if(gomoku.play_computer() == True):
            break
    
    
    gomoku.verify_game()
    
    #gomoku.board.window.mainloop()


    
