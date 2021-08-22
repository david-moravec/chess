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
        self.board.drawSquares(self.win)
        self.board.draw(self.win)
        try:
            self.board.drawValidMoves(self.win)
        except:
            pass
        pygame.display.update()

    def select(self, x, y):
        if self.selected:
            old_x = self.selected.x
            old_y = self.selected.y
            self.selected.move(x, y, self.board)
            self.board.removePiece(old_x, old_y)
            self.board.changeTurns()
            self.selected = None

        piece = self.board.getPiece(x, y)
        if piece != 0 and piece.team == self.board.turn:
            self.selected = piece
            self.selected.getValidMoves(self.board)
            return True

        return False



            
