from src.board import Board
import pygame
from src.constants import HEIGHT, WIDTH, SQUARE_SIZE
from src.game import Game

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

#def main():
#
#    game = Game(WIN)
#    game.update()
    
#
#    run = True
#    while run:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                run = False
#
#        game.update()
#
#    pygame.quit()

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
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        game.update()

if __name__ == "__main__":
    main()

