from src.board import Board
import pygame
from src.constants import HEIGHT, WIDTH
from src.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

def main():

    game = Game(WIN)
    game.update()
    

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        game.update()

    pygame.quit()

    for line in chessBoard.tiles:
        print(line)

if __name__ == "__main__":
    main()

