from position import position
from tkinter import *


class board:
    
    def __init__(self):
        self.position = position()
        
        self.matrix = [['_ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _'],
        ['_ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _'],
        ['_ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _'],
        ['_ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _'],
        ['_ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _'],
        ['_ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _'],
        ['_ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _'],
        ['_ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _'],
        ['_ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _'],
        ['_ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _'],
        ['_ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _'],
        ['_ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _'],
        ['_ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _'],
        ['_ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _'],
        ['_ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _']]
        
        self.window = Tk()


    
    def create_board(self):
    
        self.window.title("Janela 1")
        #window.bind("<Key>", key)

        
        
        for i in range(0,15):
            for j in range(0,15):
                lbl = Label(self.window, text= self.matrix[i][j])
                lbl.grid(column=j, row=i)
                self.window.update_idletasks()
                self.window.update()



    def insert_piece(self, position_x, position_y, player_id):
    
        if(player_id == 1):
            self.matrix[position_y][position_x] = ' o '
        else:
            self.matrix[position_y][position_x] = ' x '
            
        self.update_board()
        
        #print("board.insert_piece")
        
    def update_board(self):
    
        for i in range(0,15):
            for j in range(0,15):
                lbl = Label(self.window, text= self.matrix[i][j])
                lbl.grid(column=j, row=i)
                self.window.update_idletasks()
                self.window.update()
                
        #print("board.update_board")


    def play_valid(self,position):
    
        print("board.play_valid")
