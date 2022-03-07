import copy
class Board:
    def __init__(self,state=[[0,0,0],[0,0,0],[0,0,0]]):
        self.state = state
    def show(self):
        for row in range(3):
            for col in range(3):
                print(self.state[row][col],end=" ")
            print()
        print()
   
    def move(self,row,col,player):
        copi = copy.deepcopy(self.state)
        copi[row][col] = player
        return copi
    
    def isTerminal(self):
        for p in [1,2]:
            #check columns
            for c in range(3):
                x = True
                for r in range(3):
                    if(self.state[r][c] != p):
                        x = False
                if(x):
                   
                    return p
            #check rows
            for r in range(3):
                x = True
                for c in range(3):
                    if(self.state[r][c] != p):
                        x = False
                if(x):
                    
                    return p
            #check diagonals
            if(self.state[0][0] == p and self.state[1][1] == p and self.state[2][2] == p):
                return p
            if(self.state[0][2] == p and self.state[1][1] == p and self.state[2][0] == p):
                return p

        for r in range(3):
            for c in range(3):
                if(self.state[r][c] == 0):
                    return 0   
        return 3
        
if __name__ == "__main__":
    board = Board()
    board.show()
    board.state = board.move(0,0,1)
    board.state = board.move(0,1,2)
    board.state = board.move(1,1,1)
    board.state = board.move(1,2,1)
    board.state = board.move(2,0,2)
    board.state = board.move(2,1,1)
    board.state = board.move(2,2,2)
    board.show()
    print(board.isTerminal())
