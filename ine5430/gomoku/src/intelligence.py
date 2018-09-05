from board import *

class intelligence():

    def __init__(self):
    
        print("intelligence.init")

    def utility(self, nodo):
    
        print("intelligence.utility")

    def heuristic(self, nodo):
    
        print("intelligence.heuristic")

    def mini_max(self, alpha, beta, state, player, profundity):
    
        print("intelligence.mini_max")
    
    def debug_no_intelligence(self, matrix):
            
        for i in range(0,15):
            for j in range(0,15):
                if(matrix[i][j] != ' o ' and matrix[i][j] != ' x '):
                    return i, j