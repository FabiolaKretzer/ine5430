from board import *

class intelligence():

    def __init__(self):
        self.board = board()
    
        print("intelligence.init")

    def heuristic_utility(self, nodo):
    
        print("intelligence.heuristic")

    """
    def mini_max(self, alpha, beta, position_x, position_y, player, profundity):
        for i in self.board.spaces:
            if player:
                self.board.insert_piece(position_x, position_y, 1)
                temp_alpha = self.mini_max(alpha, beta, i.position_x, i.position_y, False, 0)
                alpha = max(alpha, temp_alpha)
                self.board.remove_piece(i.position_x, i.position_y)
				if alpha >= beta:
                    break 
            else:
                self.board.insert_piece(position_x, position_y, 2)
                temp_beta = self.mini_max(alpha, beta, i.position_x, i.position_y, True, 0)
                beta = max(beta, temp_beta)
                self.board.remove_piece(i.position_x, i.position_y)
				if beta >= alpha:
                    break 

        if player:
            return alpha
        return beta
    """
            
    def debug_no_intelligence(self, matrix):
            
        for i in range(0,15):
            for j in range(0,15):
                if(matrix[i][j] != ' o ' and matrix[i][j] != ' x '):
                    return i, j