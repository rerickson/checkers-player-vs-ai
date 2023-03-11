import pygame
from board import Board

class Game:
    def __init__(self, win):
        self.Selected = None
        self.board = Board()
        self.turn = 1
    
    def change_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1