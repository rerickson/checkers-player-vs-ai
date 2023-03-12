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
        # # Draw the base of the piece
        # # pygame.draw.circle(win, (128, 128, 128), (200, 250), 50)
        # pygame.draw.circle(win, (128, 128, 128), (self.x, self.y), 50)

        # # Draw the top of the piece
        # # pygame.draw.circle(win, (255, 0, 0), (200, 200), 40)
        # pygame.draw.circle(win, self.color, (self.x, self.y), 40)

        # # Draw the shine on the piece
        # # pygame.draw.circle(win, (255, 255, 255), (215, 185), 15)
        # pygame.draw.circle(win, (255, 255, 255), (self.x+15, self.y-15), 15)
# Draw the base of the piece
        # pygame.draw.circle(win, (128, 128, 128), (self.x, self.y), self.radius_base)

        # # Draw the top of the piece
        # top_y = self.y - self.radius_base + self.radius_top
        # pygame.draw.circle(win, self.color, (self.x, top_y), self.radius_top)

        # # Draw the shine on the piece
        # shine_x = self.x + int(15 * math.cos(math.pi / 4))
        # shine_y = top_y - int(15 * math.sin(math.pi / 4))
        # pygame.draw.circle(win, (255, 255, 255), (shine_x, shine_y), 15)


        # Update the display
        # pygame.display.flip()

        pygame.draw.circle(screen, BORDER_COLOR, (self.x, self.y), radius + 2) # draw a border circle wider than the piece
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius) # draw the piece