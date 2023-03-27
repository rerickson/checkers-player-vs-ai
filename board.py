from checker import Checker

class Board:
    def __init__(self):
        self.board = []
        self.player1_pieces_total = self.player2_pieces_total = 12
        self.rows = self.columns = 8
        self.complete = False

        for row in range(self.rows):
            self.board.append([])
            for col in range(self.columns):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Checker(row, col, 1))
                    elif row > 4:
                        self.board[row].append(Checker(row, col, 2))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    
    def get_checker(self, row, col):
        return self.board[row][col]

    def move(self, checker: Checker, row, col):
        self.board[checker.row][checker.col] = 0 # clear out the old space
        self.board[row][col] = checker # Set the piece to the new location
        
        # If we moved to a top or bottom row then make the checker a king
        if row == self.rows - 1 or row == 0:
            checker.make_king()

    def remove(self, checkers):
        if not checkers:
            return
        
        for checker in checkers:
            self.board[checker.row][checker.col] = 0
            if checker != 0:
                if checker.player_number == 1:
                    self.player1_pieces_total -= 1
                else:
                    self.player2_pieces_total -= 1

        winner = 0
        if(self.player1_pieces_total <= 0):
            winner = 1

        if(self.player2_pieces_total <= 0):
            winner = 2

        if(winner != 0):
            print("Congrats Player " + str(winner) + " you have won the game!")
            self.complete = True