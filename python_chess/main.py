from src.board import Board
import pygame
from src.constants import HEIGHT, WIDTH, SQUARE_SIZE, Position
from src.game import Game

import inspect

DEBUG = False

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

def get_row_col_from_mouse(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    if DEBUG:
        print(row, col)
    return Position(row, col)

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    game.update()

    while run:
        clock.tick(FPS)

#        if game.winner() != None:
#            print(game.winner())
#            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                position = get_row_col_from_mouse(pos)
                game.evaluateClick(position)
                game.update()
                game._printBoard()


if __name__ == "__main__":
    main()

