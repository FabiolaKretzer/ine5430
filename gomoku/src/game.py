from board import board
from intelligence import intelligence
import sys
import os

#funções que não permitem jogar nos extremos do jogo

def ver_r(verify_number):
    
    if(verify_number in forbidden_list_1):
        return 10000
    else:
        return verify_number
        
def ver_v(verify_number):
    
    if(verify_number in forbidden_list_1):
        return 10000
    else:
        return verify_number
        
def ver_d(verify_number):

    if(verify_number in forbidden_list_1 or verify_number in forbidden_list_2):
        return 1000
    else:
        return verify_number
        
def ver_d2(verify_number):
    
    if(verify_number in forbidden_list_3 or verify_number in forbidden_list_2):
        return 1000
    else:
        return verify_number


forbidden_list_1 = [1,16,31,46,61,76,91,106,121,136,151,166,181,196]
forbidden_list_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
forbidden_list_3 = forbidden_list_1 * 15

class game:

    def __init__(self):
    
        self.board = board()
        self.intelligence = intelligence()
        self.human_sequence_list = []
        self.computer_sequence_list = []
        
        """ 
        position 0 in list -> 2 pieces with one open side
        position 1 in list -> 2 pieces with two open side
        position 2 in list -> 3 pieces with one open side
        position 3 in list -> 3 pieces with two open side
        position 4 in list -> 4 pieces with one open side
        position 5 in list -> 4 pieces with two open side
        position 6 in list -> 5 pieces with one open side
        position 7 in list -> 5 pieces with two open side
        """
        self.list_pos_human = []
        self.list_pos_computer = []
        
    def start_game(self):
    
        print("game.start_game")

    def create_board(self):
    
        self.board.create_board()
        #print("game.create_board")
        
    def insert_pos_list(self, pos_list, x, y):
          
        map_position = y*15 + (x+1)
        
        if(map_position in self.list_pos_human or map_position in self.list_pos_computer):
            return False
        else:
            pos_list.append(map_position)
            self.board.spaces.remove(map_position)
            return True
        
        #pos_list.sort()
        #print(pos_list)

    def play_computer(self):
    
        position_y, position_x = self.intelligence.debug_no_intelligence(self.board.matrix)
        
        if(self.insert_pos_list(self.list_pos_computer,int(position_x),int(position_y)) == True):

            self.board.insert_piece(int(position_x),int(position_y),2)
            return True
        else:
            return False
        #print("game.play_computer")
    
    def play_human(self, position_x, position_y):
    
        if(self.insert_pos_list(self.list_pos_human,int(position_x),int(position_y)) == True):
            
            self.board.insert_piece(int(position_x),int(position_y),1)
            return True
        else:        
            return False
    
        #print("game.play_human")
               
    def verify_x(self, pos_list,sequence_list):
    
        if(len(pos_list) > 1):
            for i in pos_list:
                                
                #print(i)
                if(ver_r(i + 1) in pos_list and ver_r(i + 2) in pos_list and ver_r(i + 3) in pos_list and ver_r(i + 4) in pos_list):
                    sequence_list.append(5)
                elif(ver_r(i + 1) in pos_list and ver_r(i + 2) in pos_list and ver_r(i + 3) in pos_list ):
                    sequence_list.append(4)
                elif(ver_r(i + 1) in pos_list and ver_r(i + 2) in pos_list ):
                    sequence_list.append(3)
                elif(ver_r(i + 1) in pos_list ):
                    sequence_list.append(2)
                    
        sequence_list.append(10)
    
    def verify_y(self,pos_list,sequence_list):
        if(len(pos_list) > 1):
            for i in pos_list:
                #print(i)
                if(ver_v(i + 15) in pos_list and ver_v(i + (15*2)) in pos_list and ver_v(i + (15*3)) in pos_list and ver_v(i + (15*4)) in pos_list):
                    sequence_list.append(5)
                elif(ver_v(i + 15) in pos_list and ver_v(i + (15*2)) in pos_list and ver_v(i + 15*3) in pos_list):
                    sequence_list.append(4)
                elif(ver_v(i + 15) in pos_list and ver_v(i + (15*2)) in pos_list):
                    sequence_list.append(3)
                elif(ver_v(i + 15) in pos_list):
                    sequence_list.append(2)
                    
        sequence_list.append(100)
                    
    def verify_diagonal(self, pos_list,sequence_list):
        if(len(pos_list) > 1):
            for i in pos_list:
                #print(i)
                if(ver_d(i + 15+1) in pos_list and ver_d(i + (15*2)+2) in pos_list and ver_d(i + (15*3)+3) in pos_list and ver_d(i + (15*4)+4) in pos_list):
                    sequence_list.append(5)
                elif(ver_d(i + 15+1) in pos_list and ver_d(i + (15*2)+2) in pos_list and ver_d(i + (15*3)+3) in pos_list):
                    sequence_list.append(4)
                elif(ver_d(i + 15+1) in pos_list and ver_d(i + (15*2)+2) in pos_list):
                    sequence_list.append(3)
                elif(ver_d(i + 15+1) in pos_list):
                    sequence_list.append(2)
                    
        sequence_list.append(1000)
        
    def verify_inverse_diagonal(self,pos_list,sequence_list):
        if(len(pos_list) > 1):
            for i in pos_list:
                #print(i)
                if(ver_d2(i + 15-1) in pos_list and ver_d2(i + (15*2)-2) in pos_list and ver_d2(i + (15*3)-3) in pos_list and ver_d2(i + (15*4)-4) in pos_list):
                    sequence_list.append(5)
                elif(ver_d2(i + 15+1) in pos_list and ver_d2(i + (15*2)-2) in pos_list and ver_d2(i + (15*3)-3) in pos_list):
                    sequence_list.append(4)
                elif(ver_d2(i + 15-1) in pos_list and ver_d2(i + (15*2)-2) in pos_list):
                    sequence_list.append(3)
                elif(ver_d2(i + 15-1) in pos_list):
                    sequence_list.append(2)
    
        sequence_list.append(10000)
                
    def verify_game(self):
    
        self.human_sequence_list[:] = []
        self.computer_sequence_list[:] = []

        self.verify_x(self.list_pos_human,self.human_sequence_list)
        self.verify_x(self.list_pos_computer,self.computer_sequence_list)
        self.verify_y(self.list_pos_human,self.human_sequence_list)
        self.verify_y(self.list_pos_computer,self.computer_sequence_list)
        self.verify_diagonal(self.list_pos_human,self.human_sequence_list)
        self.verify_diagonal(self.list_pos_computer,self.computer_sequence_list)
        
        print("self.list_pos_human")
        print(self.list_pos_human)
        print("self.list_pos_computer")
        print(self.list_pos_computer)
        print("self.human_sequence_list")
        print(self.human_sequence_list)
        print("self.computer_sequence_list")
        print(self.computer_sequence_list)
    
        #print("game.verify_game")
       
'''

        for i in list:
            if(list.count(list(i) + 1) == 1 and list.count(list(i) + 2) == 1 and list.count(list(i) + 3) == 1 and list.count(list(i) + 4) == 1):
                print("QUINTUPLA")
            elif(list.count(list(i) + 1) == 1 and list.count(list(i) + 2) == 1 and list.count(list(i) + 3) == 1):
                print("QUADRA")
            elif(list.count(list(i) + 1) == 1 and list.count(list(i) + 2) == 1):
                print("TRIPLA")
            elif(list.count(list(i) + 1) == 1):
                print("DUPLA")


        
    def verify_game(self):
    
        self.human_sequence_list[:] = []
        self.computer_sequence_list[:] = []
    
        count_human_sequences = 0
        count_computer_sequences = 0
        
        self.list_position_human_sequence_x = []
        self.list_position_human_sequence_y = []
        self.list_position_human_sequence_diagonal = []
        self.list_position_computer_sequence_x = []
        self.list_position_computer_sequence_y = []
        self.list_position_computer_sequence_diagonal = []
        
        for i in range(0,15):
            for j in range(0,15):
                if(self.board.matrix[i][j] == ' o '):
                
                    self.verify_sequence(i,j,' o ', self.human_sequence_list, self.list_position_human_sequence_x, self.list_position_human_sequence_y, self.list_position_human_sequence_diagonal)
                
                    
        for i in range(0,15):
            for j in range(0,15):
                if(self.board.matrix[i][j] == ' x '):
                
                    self.verify_sequence(i,j,' x ', self.computer_sequence_list, self.list_position_computer_sequence_x, self.list_position_computer_sequence_y, self.list_position_computer_sequence_diagonal)
          
        print("SEQUENCIA HUMANO:")
        print(self.human_sequence_list)
        print("SEQUENCIA COMPUTADOR:")
        print(self.computer_sequence_list)
        
        if(5 in self.human_sequence_list):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("HUMANO GANHOU")
            
        if(5 in self.computer_sequence_list):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("COMPUTADOR GANHOU")
            
        print("lista posicao x human")
        print(self.list_position_human_sequence_x)
        print("lista posicao y human")
        print(self.list_position_human_sequence_y)
        print("lista posicao diagonal human")
        print(self.list_position_human_sequence_diagonal)
        print("lista posicao x computer")
        print(self.list_position_computer_sequence_x)
        print("lista posicao y computer")
        print(self.list_position_computer_sequence_y)
        print("lista posicao diagonal computer")
        print(self.list_position_computer_sequence_diagonal)


    def verify_sequence(self, i, j, char_id_player, list, list_pos_x, list_pos_y, list_pos_diagonal):
    
        count_x_sequence = 0
        count_y_sequence = 0
        count_diagonal_sequence = 0
        
        
        if i*10 + j in list_pos_x:
            print("ENTROU 1")
        else:
            for verify_x in range(0,5):                
                if(self.board.matrix[i + verify_x][j] != char_id_player):
                    break
                else:
                    count_x_sequence = count_x_sequence + 1
                    list_pos_x.append((i + verify_x)*10 + j)
            
        if(i*10 + j in list_pos_y):
            print("ENTROU 2")
        else:
            for verify_y in range(0,5):
                if(self.board.matrix[i][j + verify_y] != char_id_player):
                    break
                else:
                    count_y_sequence = count_y_sequence + 1
                    list_pos_y.append(i*10 + (j+verify_y))
                
        if(i*10 + j in list_pos_diagonal):
            print("ENTROU 3")
        else:
            for verify_diagonal in range(0,5):
                if(self.board.matrix[i + verify_diagonal][j + verify_diagonal] != char_id_player):
                    break
                else:
                    count_diagonal_sequence = count_diagonal_sequence + 1
                    list_pos_diagonal.append((i+verify_diagonal)*10 + (j+verify_diagonal))
                
        if(count_x_sequence > 1 ):
        
            list.append(count_x_sequence)
            
        if(count_y_sequence > 1):
        
            list.append(count_y_sequence)
            
        if(count_diagonal_sequence > 1):
        
            list.append(count_diagonal_sequence)
            
'''