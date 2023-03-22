import pygame
from board import Board
from player import Player

class Game:
    def __init__(self, win):
        self.Selected = None
        self.board = Board()
        self.turn = 1
        self.window = win
        self.player1 = Player(self.board, win, self)
        self.player2 = Player(self.board, win, self)
        self.player1.turn_started()
    
    def change_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1
    
    def update(self):
        self.board.draw(self.window)
        self.player1.draw_handler()
        self.player2.draw_handler()
        pygame.display.update()

    def mouse_click_handler(self):
        pos = pygame.mouse.get_pos()
        row, col = self.board.get_row_col_from_position(pos)
        if(self.turn == 1):
            current_player = self.player1
        else:
            current_player = self.player2

        checker = self.board.get_checker(row, col)
        if(checker == 0 or checker.player_number == self.turn):
            current_player.click_checker(checker, row, col)
    
    def move(self, checker, row, col):
        # update the board
        self.board.move(checker, row, col)

        # update the checker
        checker.move(row, col)

        # once a move is made it changes turns
        self.change_turn()
