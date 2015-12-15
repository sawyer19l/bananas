
import random

EMPTY,X,O = ' ','X','O'
class Board(object):
    
    def __init__(self):
        self.board = [EMPTY]*9
    
    def __str__(self):
        return '\n-----\n'.join(['%s|%s|%s'%x for x in zip(*[iter(self.board)]*3)])
    
    def count(self):
        return sum(map(lambda x: x!=EMPTY, self.board))
    
    def move(self,pos,player):
        if self.board[pos] == EMPTY:
            self.board[pos] = player
            return True
        return False
        
    def undo(self,pos,player):
        # player is only here for symmetry, other games may require this though.
        self.board[pos] = EMPTY    
        
    def candidates(self):
        return [i for i,x in enumerate(self.board) if x==EMPTY]       
            
    def check_win(self):
        b = self.board
        # A helper function
        def _check_row(i1,i2,i3): return b[i1]!=EMPTY and b[i1]==b[i2]==b[i3]    
    
        if _check_row(0,1,2): return b[0]
        if _check_row(3,4,5): return b[3]
        if _check_row(6,7,8): return b[6]
        if _check_row(0,3,6): return b[0]
        if _check_row(1,4,7): return b[1]
        if _check_row(2,5,8): return b[2]
        if _check_row(0,4,8): return b[0]
        if _check_row(2,4,6): return b[2]
    
# In other languages this is called an interface, it's not an actual class
# and its a template for other classes to implement. Python doesn't support
# interfaces, but it's still useful to specify methods that subclasses should
# implement. Also see polymorphism, which we will use thoughout.
# https://en.wikipedia.org/wiki/Polymorphism_(computer_science)
class IPlayer(object):
    def __init__(self, symbol):
        self.symbol = symbol
    def move(self, board, opponent):
        raise Exception('must be implemented')
    def name(self):
        return self.__class__.__name__
    def __str__(self):
        return self.symbol
        

# Here we specify which class we are inheriting from, we are 'pretending' to
# be implementing an interface.
class HumanPlayer(IPlayer):
    # This class is supposed to write the method move, if we don't
    # the superclass will throw an exception
    def move(self, board, opponent):
        print board
        # Allow the player to use the numpad
        numpad = [7,8,9,4,5,6,1,2,3]
        while True:
            try:
                s = numpad.index(int(raw_input('Enter a move (%s): '%self.symbol)))
                while not board.move(s,self):
                    print 'Sorry that square is taken.', 
                    s = numpad.index(int(raw_input('Enter a move (%s): '%self.symbol)))
                return True
            except:
                "Enter a number, idiot"
        
class MinimaxAI(IPlayer):
    # This is the syntax for a 'private' function, that shouldn't be used
    # outside of this class. In python it is not truly private.
    def _minimax(self, board, player, opponent):

        win = board.check_win()
        if win == self: return 1
        if win and win!=self: return -1
        if board.count() == 9: return 0

        best = 2-4*(player == self)
        for pos in board.candidates():
            board.move(pos, player)
            val = self._minimax(board, opponent, player)
            board.undo(pos, player)
            if   self == player:   best = max(best, val)
            elif self == opponent: best = min(best, val)  
            
        return best
        
    def move(self, board, opponent):
        if board.count() == 0:
            board.move(0,self)
        else:
            # Randomly choose one optimal move
            options = []
            for pos in board.candidates():
                board.move(pos, self)
                options.append((self._minimax(board, opponent, self),pos))
                board.undo(pos, self)            
            options = filter(lambda (x,y):x==max(options)[0],options)
            board.move(random.choice(options)[1], self)
            

def do_game(player1, player2):
    board = Board()
    start = random.randint(0,1)
    while board.count() < 9:
        if start: player1.move(board,player2)
        else: player2.move(board,player1)
        start = 1-start
        winner = board.check_win()
        if winner: return winner.name()+' Wins'
    return 'Tie Game'
           
        
# This is here to allow 'import tictactoe' without running the code below,
# when it's being imported the __name__ variable is set to something else.
if __name__ == '__main__':
    
    # Use the numpad to play (numbers correspond to grid, not index)
    while True:
        p1 = HumanPlayer(X)
        p2 = MinimaxAI(O)
        print do_game(p1,p2)
