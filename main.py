import pygame

from game import Game

GAME_SIDE = 800
WINDOW = pygame.display.set_mode((GAME_SIDE,GAME_SIDE))

pygame.display.set_caption('Checkers - Can you beat the AI?')

def main():
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or game.board.complete:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.mouse_click_handler()

        game.update()

        if(run != True):
            pygame.quit()
        
main()