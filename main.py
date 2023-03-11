import pygame

from game import Game

WINDOW = pygame.display.set_mode((800,800))
pygame.display.set_caption('Checkers - Can you beat the AI?')

def main():
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


main()