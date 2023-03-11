import pygame

class Checker:
    def __init__(self, row, col, playerNumber):
        self.row = row
        self.col = col
        self.king = False
        self.x = 0
        self.y = 0
        if(playerNumber == 1):
            self.color = (255, 0, 0)
        else:
            self.color = (255, 255, 255)
            
        self.calc_center()

    def calc_center(self):
        self.x = 100 * self.row + 50
        self.y = 100 * self.row + 50

    def draw(self, win):
        radius = 50 - 15
        pygame.draw.circle(win, (128,128,128), (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)