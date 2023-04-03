from __future__ import annotations
from board import Board
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from checker import Checker
    from game import Game

class Player:
    def __init__(self, win, game): # todo move board and window logic out of here
        self.selected: Checker = None
        self.valid_moves = {}
        self.win = win
        self.game: Game = game

    def click_checker(self, checker: Checker, row: int, col: int, board: Board):
        if(self.selected and checker == 0):
            self._move(row, col, board)
            return
        
        if(checker == 0):
            return
        
        self.selected = checker
        self.valid_moves = board.get_valid_moves(checker)
        
    def _move(self, row: int, col: int, board: Board):
        if self.selected and (row, col) in self.valid_moves:
            self.game.move(self.selected, row, col)
            jumpedCheckers = self.valid_moves[(row, col)]
            board.remove(jumpedCheckers)
            self.valid_moves = {}
    
    def change_turn(self):
        self.selected = None
    