from checker import Checker

class Board:
    def __init__(self):
        self.board = []
        self.checkers = [0,12,12]
        self.kings = [0,0,0]
        self.rows = self.columns = 8
        self.complete = False
        self.winner = 0

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
            self.kings[checker.player_number] += 1
            # print("New eval: " + str(self.evaluate()))

    def remove(self, checkers: Checker):
        if not checkers:
            return
        
        for checker in checkers:
            self.board[checker.row][checker.col] = 0
            if checker != 0:
                self.checkers[checker.player_number] -= 1

        # todo - we also need to check if there are no valid moves
        if(self.checkers[1] <= 0):
            self.winner = 2

        if(self.checkers[2] <= 0):
            self.winner = 1

        if(self.winner != 0):
            print("Congrats Player " + str(self.winner) + " you have won the game!")
            self.complete = True

        # print("New eval: " + str(self.evaluate()))

    def evaluate(self):
        return self.checkers[1] - self.checkers[2] + (self.kings[1] * 0.5 - self.kings[2] * 0.5)
    
    def get_all_checkers(self, player_number):
        checkers = []
        for row in self.board:
            for checker in row:
                if checker != 0 and checker.player_number == player_number:
                    checkers.append(checker)
        return checkers