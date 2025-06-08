
from abc import ABC,abstractmethod



class Symbol:
    X= "X"
    O="O"
    EMPTY=""





class Position:
    def __init__(self,row,column):
        self.row = row
        self.column = column





class GameStrategy(ABC):
    @abstractmethod
    def make_move(self):
        pass

class HumanPlayerStrategy(GameStrategy):
    def make_move(self,board,name):
        print(name, ", Please make your move")
        while True:
            r = int(input("Enter row grid : "))
            c = int(input("Enter column grid : "))
            if not board.is_move_valid(Position(r,c)):
                print("Invalid Move, Please make a valid one")
                continue
            return Position(r,c)



class Player:
    def __init__(self,symbol,name,strategy):
        self.symbol = symbol 
        self.name = name
        self.strategy = strategy 

    def make_move(self,board):
        pos = self.strategy.make_move(board,self.name)
        board.make_move(pos,self.symbol)





class GameState(ABC):
    @abstractmethod
    def is_game_over(self):
        pass

class XTurnState(GameState):
    def is_game_over(self):
        return False

class OTurnState(GameState):
    def is_game_over(self):
        return False
    
class XWonState(GameState):
    def is_game_over(self):
        return True
    
class OWonState(GameState):
    def is_game_over(self):
        return True
    
class DrawState(GameState):
    def is_game_over(self):
        return True
    
class GameContext:
    def __init__(self):
        self.currentState = XTurnState()

    def set_state(self,state):
        self.currentState = state

    def get_current_state(self):
        return self.currentState
    
    def is_game_over(self) -> bool:
        return self.currentState.is_game_over()




    



class Board:
    def __init__(self,grid_size):
        self.grid_size = grid_size
        self.board = [[Symbol.EMPTY] * grid_size for i in range(grid_size)]

    def display(self):
        for row in self.board:
                print(row)

    def make_move(self,pos,symbol):
        self.board[pos.row][pos.column] = symbol

    def is_move_valid(self, position):
        if position.row >= 0 and position.row <= self.grid_size-1 \
            and position.column >= 0 and position.column <= self.grid_size-1 \
            and self.board[position.row][position.column] == Symbol.EMPTY:
            return True
        return False

    def isGameWon(self,symbol):
        for row in self.board:
            if all(cell == symbol for cell in row):
                return True
            
        for col in range(self.grid_size):
            if all(self.board[row][col] == symbol for row in range(self.grid_size)):
                return True
            
        # Check diagonals
        if all(self.board[i][i] == symbol for i in range(self.grid_size)):
            return True
        
        if all(self.board[i][self.grid_size - i- 1] == symbol for i in range(self.grid_size)):
            return True
        return False
    
    def is_full(self):
        return all(cell != Symbol.EMPTY for row in self.board for cell in row)

    



class TicTacToe:
    def __init__(self,grid_size,player_x,player_o):
        self.grid_size = grid_size
        self.board = Board(grid_size)
        self.player_x = player_x
        self.player_o = player_o
        self.game_context = GameContext()


    def switch_Player(self):
        if isinstance(self.game_context.get_current_state(), XTurnState):
            self.game_context.set_state(OTurnState())
        else:
            self.game_context.set_state(XTurnState())


    def play(self):
        while not self.game_context.is_game_over():
            self.board.display()

            if isinstance(self.game_context.get_current_state(), XTurnState):
                self.player_x.make_move(self.board)
                if self.board.isGameWon(self.player_x.symbol):
                    self.game_context.set_state(XWonState())
                    break
            else: 
                self.player_o.make_move(self.board)
                if self.board.isGameWon(self.player_o.symbol):
                    self.game_context.set_state(OWonState())
                    break

            if self.board.is_full():
                self.game_context.set_state((DrawState()))
                break
            self.switch_Player()


    def announce_result(self):
        if isinstance(self.game_context.get_current_state(), XWonState):
            print("Player X wins!")
        elif isinstance(self.game_context.get_current_state(), OWonState):
            print("Player O wins!")
        elif isinstance(self.game_context.get_current_state(), DrawState):
            print("It's a draw!")
        else:
            print("Game is still in progress.")

            

if __name__ == "__main__":

    grid_size = int(input("Enter the game grid size :"))


    player1Name = (input("Enter the first players name (Would be assigned symbol X):"))
    player2Name = (input("Enter the second players name (Would be assigned symbol O):"))


    player1 = Player(Symbol.X,player1Name,HumanPlayerStrategy())
    player2 = Player(Symbol.O,player2Name,HumanPlayerStrategy())


    ticTacToe = TicTacToe(grid_size,player1,player2)
    ticTacToe.play()
    ticTacToe.announce_result()





