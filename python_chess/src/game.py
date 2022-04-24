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

    def __movePiece(self, move):
        for key in self._valid_moves.keys():
            if move in self._valid_moves[key]:
                self.__selected.move(move)
                for piece in self._pieces:
                    if(    piece.position() == move
                       and piece.team() != self.turn
                      ):
                        piece.die()

    def evaluateClick(self, position):
        #if we already selected a piece, we want to move it. Currently does not support change of pieces, so if we choose a piece we HAVE to move it
        breakpoint()
        if self.__selected:
            self.__movePiece(position)
            if self.__selected.moved:
                self.__changeTurns()
                self.__selected.resetMoved()
                self._resetValidMoves()

            self.__selected = None
            position = None

        #if we have no piece selected, select current piece
        else:
            for piece in self._pieces_alive:
                if (    piece.position() == position
                    and piece.team() == self.turn
                   ):
                        self.__selected = piece
                        self.__selected.old_position = position
                        self._getValidMoves(self.__selected)

            if DEBUG:
                print(self.evaluateClick.__name__, "\n")
                print("selected Piece:", self.__selected)
                print("valid moves", self._valid_moves)



    def __changeTurns(self):
        if self.turn == WHITE:
            self.turn = BLUE
        else:
            self.turn = WHITE
