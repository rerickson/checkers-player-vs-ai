from __future__ import annotations
from board import Board
from player import Player
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from checker import Checker

class Game:
    def __init__(self, win):
        self.Selected: Checker = None
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

    def mouse_click_handler(self, pos):
        row, col = pos

        if(self.turn == 1):
            current_player = self.player1
        else:
            current_player = self.player2

        checker: Checker = self.board.get_checker(row, col)
        if(checker == 0 or checker.player_number == self.turn):
            current_player.click_checker(checker, row, col)
    
    def move(self, checker: Checker, row: int, col: int):
        # update the board
        self.board.move(checker, row, col)

        # update the checker
        checker.move(row, col)

        # once a move is made it changes turns
        self.change_turn()
