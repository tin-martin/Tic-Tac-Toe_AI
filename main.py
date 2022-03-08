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
        self.moves = []
        self.best_child = None
        self.best_move = None
        

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
                    self.moves.append([r,c])
        
        return self.childs,self.moves

class MiniMax:
    #initiate root node
    def __init__(self,root):
        #initalize root state, depth of search
        self.root = root
       # self.maxDepth = maxDepth

    def maximizer(self,node,depth=0):
        winner = node.board.isTerminal()
        if(winner != 0):     
            if(self.root.player == winner):
                node.score = 1  
            elif(winner == 3):
                node.score = 0 
            else:
                node.score = -1 
        else:
            childs,moves = node.find_childs()
            max_score = -math.inf
            bc_depth = math.inf
            best_child = None
            best_move = None
            for child,move in zip(childs,moves):
                self.minimizer(child,depth+1)
                if(child.score > max_score):
                    max_score = child.score - (depth/1000)
                    best_child = child
                    best_move = move
            node.score = max_score
            node.best_child = best_child
            node.best_move = best_move

    def get_state(self,state):
        stack = []
        stack.append(root_node)
        while(len(stack) > 0):
            node = stack.pop()
            for child in node.childs: 
                if(child.board.state == state):
                    return child
                stack.append(child)

    def minimizer(self,node,depth=0):
        winner = node.board.isTerminal()
        if(winner != 0):     
            if(winner == self.root.player):
                node.score = 1 
            elif(winner == 3):
                node.score = 0 
            else:
                node.score = -1 
        else:
            childs,moves = node.find_childs()
            min_score = math.inf
            bc_depth = -math.inf
            best_child = None
            best_move = None
            for child,move in zip(childs,moves):
                self.maximizer(child,depth+1)
                if(child.score <= min_score):
                   min_score = child.score - (depth/1000)
                   best_child = child
                   best_move = move
                
            node.score = min_score
            node.best_child = best_child
            node.best_move = best_move

    

          
if __name__ == "__main__":
    #Player 1 starts first

    root_board = Board()
    
    root_node = Node(None,root_board,1)
    node = root_node
    minimax = MiniMax(root_node)
    minimax.maximizer(node)
    print("Computer Move: "+str(node.best_move[0])+","+str(node.best_move[1]))
    node.best_child.board.show()
    node = node.best_child
    

    while(node.board.isTerminal() == 0):
        try:
            move = input("Enter move (row,col): ").split(",")
            state = node.board.move(int(move[0]), int(move[1]), 2)
        except:
            continue
        
        node = minimax.get_state(state)
        node.board.show()
        
        print("Computer Move: "+str(node.best_move[0])+","+str(node.best_move[1]))
        node.best_child.board.show()
        
        node = node.best_child
    
    
