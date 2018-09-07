from board import *

class intelligence():

    def __init__(self):
        self.board = board()
    
    def heuristic_utility(self, sequence_list): 
        heuristic = 10000000 * 5 * sequence_list[4] + 100000 * 4 * sequence_list[2] + 1000 * 3 * sequence_list[1] + 10 * 2 * sequence_list[0]  
        return heuristic
    
        #print("intelligence.heuristic")

    def mini_max(self, alpha, beta, player, profundity, sequence_list):

        if profundity == 0 or self.is_end_play():
            return (player, self.heuristic(sequence_list))

        #human
        if player == 1:
            best = alpha
            for i in range(0, 15):
                for j in range(0, 15):
                    if(self.board.matrix[i][j] != ' o ' and self.board.matrix[i][j] != ' x '):
                        self.board.insert_piece(i, j, player)
                        value = self.mini_max(alpha, beta, 2, profundity - 1, sequence_list)
                        self.board.remove_piece(i, j)
                        if best < value:
                            best = value
                            op_x, op_y = i, j
                        if beta <= best:
                            break
        #computer
        else:
            best = beta
            for i in range(0, 15):
                for j in range(0, 15):
                    if(self.board.matrix[i][j] != ' o ' and self.board.matrix[i][j] != ' x '):
                        self.board.insert_piece(i, j, player)
                        value = self.mini_max(alpha, beta, 1, profundity - 1, sequence_list)
                        self.board.remove_piece(i, j)
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