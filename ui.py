import pygame
import math
from checker import Checker

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game
    from board import Board
    
BOARD_COLOR = (0,100,0)
BOARD_SECOND_COLOR = (144, 238, 144)
SQUARE_SIZE = 100
PLAYER1_COLOR = (255, 0, 0)
PLAYER2_COLOR = (255, 255, 255)
BLACK = (0,0,0)

class UI:
    
    def __init__(self, screen, game):
        self.board : Board = game.board
        self.game: Game = game
        self.screen = screen

    def update(self):
        self.draw()
        pygame.display.update()

    def draw(self):
        self.draw_squares()
        self.draw_checkers()
        if(self.game.current_player != None and self.game.current_player.selected != None):
            valid_moves = self.game.current_player.get_valid_moves(self.game.current_player.selected)
            self.draw_valid_moves(valid_moves)
            self.draw_selected(self.game.current_player.selected)

    def draw_squares(self):
        self.screen.fill(BOARD_COLOR)
        for row in range(self.board.rows):
            for col in range(row % 2, self.board.columns, 2):
                # since everything is BOARD_COLOR we just have to draw the non BOARD_COLOR squares
                pygame.draw.rect(self.screen, BOARD_SECOND_COLOR, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_checkers(self):
        for row in range(self.board.rows):
            for col in range(self.board.columns):
                checker = self.board.get_checker(row, col)
                if checker != 0:
                    self.draw_checker(checker) # todo move draw logic here

    def draw_checker(self, checker: Checker):
        radius = 35
        pygame.draw.circle(self.screen, BLACK, (checker.x, checker.y), radius + 2) # draw a border circle wider than the piece
        pygame.draw.circle(self.screen, self.get_checker_color(checker), (checker.x, checker.y), radius) # draw the piece

        if(checker.king):
            star_radius = 25
            # Draw star
            num_points = 5
            star_points = []
            for i in range(num_points * 2):
                angle = i * math.pi / num_points
                radius = star_radius if i % 2 == 0 else star_radius / 2
                x = radius * math.cos(angle)
                y = radius * math.sin(angle)
                star_points.append((int(x) + checker.x, int(y) + checker.y))
            pygame.draw.polygon(self.screen, BLACK, star_points)

    def get_checker_color(self, checker: Checker):
        if(checker.player_number == 1):
            return PLAYER1_COLOR
        
        return PLAYER2_COLOR

    def get_row_col_from_mouse(self):
        pos = pygame.mouse.get_pos()
        return self.get_row_col_from_position(pos)

    def get_row_col_from_position(self, pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col
    
    def draw_valid_moves(self, valid_moves):
        for move in valid_moves:
            row, col = move
            pygame.draw.circle(self.screen, (0, 0, 255), (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def draw_selected(self, checker: Checker):
        pygame.draw.circle(self.screen, (0,255,0), (checker.x, checker.y), 50, 5)
