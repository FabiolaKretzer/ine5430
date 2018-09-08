from board import *

class intelligence():

    def __init__(self):
        self.board = board()
    
    def heuristic_utility(self, human_sequence_list, computer_sequence_list): 
        heuristic = (10000000 * 5 * computer_sequence_list[3] + 100000 * 4 * computer_sequence_list[2] + 1000 * 3 * computer_sequence_list[1] + 10 * 2 * computer_sequence_list[0])  - (10000000 * 5 * human_sequence_list[3] + 100000 * 4 * human_sequence_list[2] + 1000 * 3 * human_sequence_list[1] + 10 * 2 * human_sequence_list[0])
        return heuristic
    
        #print("intelligence.heuristic")

    def mini_max(self, alpha, beta, player, profundity, human_sequence_list, computer_sequence_list):

        if profundity == 0 or self.is_end_play():
            return (0, player, self.heuristic_utility(human_sequence_list, computer_sequence_list))

        for i in range(0, 15):
            for j in range(0, 15):
                #human
                if player == 1:
                    best = alpha
                    if(self.board.matrix[i][j] != ' o ' and self.board.matrix[i][j] != ' x '):
                        #simulate movement the piece
                        #self.board.insert_piece(i, j, player)
                        #self.board.update_board()
                        map_position = j*15 + (i+1)
                        human_sequence_list.append(map_position)
                        ignore, play, value = self.mini_max(alpha, beta, 2, profundity - 1, human_sequence_list, computer_sequence_list)
                        #remove simulate movement the piece
                        #self.board.remove_piece(i, j)
                        #self.board.update_board()
                        human_sequence_list.remove(map_position)
                        if best < value:
                            best = value
                            op_x, op_y = i, j
                        if beta <= best:
                            break
                #computer
                else:
                    best = beta
                    if(self.board.matrix[i][j] != ' o ' and self.board.matrix[i][j] != ' x '):
                        #simulate movement the piece
                        #self.board.insert_piece(i, j, player)
                        #self.board.update_board()
                        map_position = j*15 + (i+1)
                        computer_sequence_list.append(map_position)
                        ignore, play, value = self.mini_max(alpha, beta, 1, profundity - 1, human_sequence_list, computer_sequence_list)
                        #remove simulate movement the piece
                        #self.board.remove_piece(i, j)
                        #self.board.update_board()
                        computer_sequence_list.remove(map_position)
                        if best > value:
                            best = value
                            op_x, op_y = i, j
                        if best <= alpha:
                           break

        return (op_x, op_y, best)

    def is_end_play(self):
        return False
            
    def debug_no_intelligence(self, matrix):
            
        for i in range(0,15):
            for j in range(0,15):
                if(matrix[i][j] != ' o ' and matrix[i][j] != ' x '):
                    return i, j