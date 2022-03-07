

#https://www.youtube.com/watch?v=wylMwU1wEOM
#fck life
import math
from board import Board

#node:
    #board (current state)
    #player (the one whose about to make the move)
    #score ( score possible for this position if everyone plays perfectly from the pos)

class Node:
    def __init__(self,parent,board,player):
        self.board = board
        self.parent = parent
        self.player = player
        self.score = 0
        self.childs = []
        self.best_child = None

    def find_childs(self):
        #finds all possible childs
        state = self.board.state
        for r in range(3):
            for c in range(3):
                if(state[r][c] == 0):
                    nboard = self.board.move(r,c,self.player)
                    nplayer = None
                    if(self.player == 1):
                        nplayer = 2
                    else:
                        nplayer = 1
                    child = Node(self,Board(nboard),nplayer)
                    self.childs.append(child)
        
        return self.childs

class MinMax:
    #initiate root node
    def __init__(self,root):
        #initalize root state, depth of search
        self.root = root
       # self.maxDepth = maxDepth

    def config(self,root):
        self.root = root

    def max_move(self,node,depth=0):
        winner = node.board.isTerminal()
        if(winner != 0):     
            if(self.root.player == winner):
                node.score = 1 - (depth/1000)
            elif(winner == 3):
                node.score = 0 - (depth/1000)
            else:
                node.score = -1 - (depth/1000)
        else:
            childs = node.find_childs()
            max = -math.inf
            C = None
            for child in childs:
                self.min_move(child,depth+1)
                if(child.score > max):
                    max = child.score
                    C = child

            node.score = max
            node.best_child = C
            
          

    def min_move(self,node,depth=0):
        winner = node.board.isTerminal()
        if(winner != 0):     
            if(winner == self.root.player):
                node.score = 1 - (depth/1000)
            elif(winner == 3):
                node.score = 0 - (depth/1000)
            else:
                node.score = -1 - (depth/1000)
        else:
            childs = node.find_childs()
            min = math.inf
            C = None
            for child in childs:
                self.max_move(child,depth+1)
                if(child.score < min):
                    min = child.score
                    C = child
            node.score = min
            node.best_child = C
        

       
          
if __name__ == "__main__":
    #Player 1 starts first

    root_board = Board()
    
    root_node = Node(None,root_board,1)
    node = root_node
    minmax = MinMax(root_node)
    minmax.max_move(node)
    node.best_child.board.show()
    node = node.best_child

    while(node.board.isTerminal() == 0):
        try:
            move = input("Enter move (r,c): ").split(",")
            node.board.state = node.board.move(int(move[0]), int(move[1]), 2)
        except:
            continue

        node.board.show()
        

        node = Node(None,node.board,1)
        minmax = MinMax(node)
        minmax.max_move(node)
        node.best_child.board.show()
        node = node.best_child
        
     #   minmax.min_move(node)
     #   node.best_child.board.show()

      #  node = node.best_child

    #root_node.best_child.best_child.board.show()
