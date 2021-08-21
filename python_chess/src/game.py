import pygame
from src.board import Board
from src.constants import WHITE


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}

    def update(self):
        self.board.draw_squares(self.win)
        pygame.display.update()
