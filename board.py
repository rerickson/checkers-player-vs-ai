import pygame
from checker import Checker, PLAYER1_COLOR, PLAYER2_COLOR

BOARD_COLOR = (0,100,0)
BOARD_SECOND_COLOR = (144, 238, 144)
SQUARE_SIZE = 100

class Board:
    def __init__(self):
        self.board = []
        self.player1_pieces_total = player2_pieces_total = 12
        self.rows = self.columns = 8
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


    def draw(self, win):
        self.draw_squares(win)
        self.draw_checkers(win)

    def draw_squares(self, win):
        win.fill(BOARD_COLOR)
        for row in range(self.rows):
            for col in range(row % 2, self.columns, 2):
                pygame.draw.rect(win, BOARD_SECOND_COLOR, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) # since everything is BOARD_COLOR we just have to draw the non BOARD_COLOR squares

    def draw_checkers(self, win):
        for row in range(self.rows):
            for col in range(self.columns):
                checker = self.board[row][col]
                if checker != 0:
                    checker.draw(win)
    
    def get_row_col_from_position(self, pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col
    
    def get_checker(self, row, col):
        return self.board[row][col]
