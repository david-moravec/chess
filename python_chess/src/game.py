import pygame
from src.board import Board
from src.constants import WHITE, BLUE, DEBUG

DEBUG = False

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

    def select(self, row, col):
        #if we already selected a piece, we want to move it. Currently does not support change of pieces, so if we choose a piece we HAVE to move it
        if self.selected:
            self.selected.move((row, col), self.board)

            old_row = self.selected.row
            old_col = self.selected.col
            if row != old_row and col != old_col:
                self.board.removePiece(old_row, old_col)
            self.board.changeTurns()
            self.selected = None

        #if we have no piece selected, select current piece
        else:
            piece = self.board.getPiece(row, col)
            if piece != 0 and piece.team == self.board.turn:
                self.selected = piece
                self.selected.getValidMoves(self.board) #gets the valid moves of a piece
            if DEBUG:
                print(self.select.__name__, self.selected)
