import pygame

from game import Game

GAME_SIDE = 800
WINDOW = pygame.display.set_mode((GAME_SIDE,GAME_SIDE))

pygame.display.set_caption('Checkers - Can you beat the AI?')

def main():
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.mouse_click_handler()
                # pos = pygame.mouse.get_pos()
                # row, col = get_row_col_from_mouse(pos)
                # game.select(row, col)

        game.update()
        
main()