import pygame
from src.board import Board
from src.constants import WHITE, BLUE, DEBUG

#interface between pyGame and board

DEBUG = False

class Game(Board):
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        self.__selected = None
        Board.__init__(self)
        self.turn = WHITE

    def update(self):
        self._update()
        pygame.display.update()

    def evaluateClick(self, position):
        #if we already selected a piece, we want to move it. Currently does not support change of pieces, so if we choose a piece we HAVE to move it
        if self.__selected:
            self.__selected.move(position, self.board)
            if self.__selected.moved:
                self.__changeTurns()
                self.__selected.resetMoved()
            self.__selected = None

        #if we have no piece selected, select current piece
        else:
            piece = self._getPiece(position)
            if piece != 0 and piece.team == self.turn:
                self.__selected = piece
                self.__selected.old_dest = position
                self.__selected.getValidMoves() #gets the valid moves of a piece

            if DEBUG:
                print(self.select.__name__, self.__selected)
                print(self.select.__name__, self._valid_moves)

    def __changeTurns(self):
        if self.turn == WHITE:
            self.turn = BLUE
        else:
            self.turn = WHITE
