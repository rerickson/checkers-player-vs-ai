import pygame
import math

PLAYER1_COLOR = (255, 0, 0)
PLAYER2_COLOR = (255, 255, 255)
BORDER_COLOR = (0,0,0)

class Checker:
    def __init__(self, row, col, player_number):
        self.row = row
        self.col = col
        self.king = False
        self.x = 0
        self.y = 0
        self.radius_base = 50
        self.radius_top = 40
        self.player_number = player_number
        if(player_number == 1):
            self.color = PLAYER1_COLOR
        else:
            self.color = PLAYER2_COLOR

        self.calc_center()

    def calc_center(self):
        self.x = 100 * self.col + 50
        self.y = 100 * self.row + 50

    def draw(self, screen):
        radius = 35
        pygame.draw.circle(screen, BORDER_COLOR, (self.x, self.y), radius + 2) # draw a border circle wider than the piece
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius) # draw the piece

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_center()