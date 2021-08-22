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
        self.valid_moves = {}

    def update(self):
        self.board.draw_squares(self.win)
        self.board.draw(self.win)
        pygame.display.update()

    def select(self, x, y):
        if self.selected:
            pass

        piece = self.board.getPiece(x, y)
        if piece != 0 and piece.team == self.board.turn:
            self.selected = piece
            self.selected.getValidMoves(self.board)
            return True

        return False



            
