import pygame

PLAYER1_COLOR = (255, 0, 0)
PLAYER2_COLOR = (255, 255, 255)
BORDER_COLOR = (0,0,0)

class Checker:
    def __init__(self, row, col, playerNumber):
        self.row = row
        self.col = col
        self.king = False
        self.x = 0
        self.y = 0
        if(playerNumber == 1):
            self.color = PLAYER1_COLOR
        else:
            self.color = PLAYER2_COLOR

        self.calc_center()

    def calc_center(self):
        self.x = 100 * self.col + 50
        self.y = 100 * self.row + 50

    def draw(self, win):
        radius = 35
        pygame.draw.circle(win, BORDER_COLOR, (self.x, self.y), radius + 2) # draw a border circle wider than the piece
        pygame.draw.circle(win, self.color, (self.x, self.y), radius) # draw the piece