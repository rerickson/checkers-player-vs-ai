import pygame

class Board:
    def __init__(self):
        self.board = []
        self.player1_pieces_total = player2_pieces_total = 12
        self.rows = self.columns = 8

        for row in range(self.rows):
            self.board.append([])
            for col in range(self.columns):
                if col % 2 == ((row + 1) % 2): # Only count the valid positions - TODO could simplify to 8*4 grid internally
                    if(row < 3): # Player one starting pieces (White)
                        self.board[row].append(Checker(row, col, 1))
                elif row > 4: # Player 2 starting pieces (Red)
                    self.board[row].append(Checker(row, col, 2))
                else:
                    self.board[row].append(0)
            else:
                self.board[row].append(0)

                

