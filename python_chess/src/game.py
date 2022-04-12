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
        if move in self._valid_moves:
            self.__selected.move(move)

    def _removePiece(self, old_position, new_position):
        if isinstance(self._getPiece(new_position), Piece):
            self.board[old_position[0]][old_position[1]] = 0
            if DEBUG:
                print("removing Piece on", old_position)

    def evaluateClick(self, position):
        #if we already selected a piece, we want to move it. Currently does not support change of pieces, so if we choose a piece we HAVE to move it
        if self.__selected:
            self.__movePiece(position)
            if self.__selected.moved:
                self.__changeTurns()
                self.__selected.resetMoved()
                self._resetValidMoves()

            self.__selected = None

        #if we have no piece selected, select current piece
        else:
            for piece in self._pieces:
                #print(piece)
                #print(piece.position())
                #print(position)
                #print(piece.team() == self.turn)
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
