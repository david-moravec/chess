import pygame
import os
from abc import ABC, abstractmethod

from src.constants import SCALE_FACTOR, BLUE, WHITE, DEBUG, Position

knight_black = pygame.image.load("src/figures-graphics/black-knight.png")
king_black = pygame.image.load("src/figures-graphics/black-king.png")
queen_black = pygame.image.load("src/figures-graphics/black-queen.png")
bishop_black = pygame.image.load("src/figures-graphics/black-bishop.png")
rook_black = pygame.image.load("src/figures-graphics/black-rook.png")
pawn_black = pygame.image.load("src/figures-graphics/black-pawn.png")

knight_white = pygame.image.load("src/figures-graphics/white-knight.png")
king_white = pygame.image.load("src/figures-graphics/white-king.png")
queen_white = pygame.image.load("src/figures-graphics/white-queen.png")
bishop_white = pygame.image.load("src/figures-graphics/white-bishop.png")
rook_white = pygame.image.load("src/figures-graphics/white-rook.png")
pawn_white = pygame.image.load("src/figures-graphics/white-pawn.png")

DEBUG = False

class Piece(ABC):
    def __init__(self, position, team):
        self._team  = team
        self._old_position = (0,0)
        self._position = (0,0)
        self._potential_moves = {}
        self.move(position)
        self.moved = False
        self.alive = True

    def position(self):
        return (self._position)

    def oldPosition(self):
        return self.__old_position

    def team(self):
        return self._team

    def getPotentialMoves(self):
        return self._potential_moves


    def move(self, position):
        self._position = position
        self.moved = True

    def resetMoved(self):
        self.moved = False

    def die(self):
        self.alive = False

    def didMove(self, position):
        #print(position, self.oldPosition())
        return position != self.oldPosition()

    def resetValidMoves(self):
        self.valid_moves = []

    @abstractmethod
    def getPotentialMoves(self):
        pass

    def cropPotentialMoves(self):
        cropped_moves = {}
        for key in self.potential_moves.keys():
            cropped_moves[key] = []
            for move in self.potential_moves[key]:
                if (   move.row > 7 or move.row < 0 
                    or move.col > 7 or move.col < 0
                   ):
                    continue
                elif (move == self.position()):
                    continue
                else:
                    cropped_moves[key].append(move)
        return cropped_moves

    def getImage(self):
        if self._team == BLUE:
            return self.__image_black
        elif self._team == WHITE:
            return self.__image_white

class Knight(Piece):

    def __init__(self, position, team):
        Piece.__init__(self, position, team)
        self.__image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
        self.__image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __repr__(self):
        return "n"

    def getPotentialMoves(self):
        self.potential_moves = {'dummy' : []}
        row = self._position.row
        col = self._position.col

        self.potential_moves['dummy'].append(Position(row + 2, col + 1))
        self.potential_moves['dummy'].append(Position(row + 1, col + 2))

        self.potential_moves['dummy'].append(Position(row - 2, col + 1))
        self.potential_moves['dummy'].append(Position(row - 1, col + 2))

        self.potential_moves['dummy'].append(Position(row + 2, col - 1))
        self.potential_moves['dummy'].append(Position(row + 1, col - 2))
        
        self.potential_moves['dummy'].append(Position(row - 2, col - 1))
        self.potential_moves['dummy'].append(Position(row - 1, col - 2))

        return self.cropPotentialMoves()

    def getImage(self):
        if self._team == BLUE:
            return self.__image_black
        elif self._team == WHITE:
            return self.__image_white

class Bishop(Piece):
    __image_black = pygame.transform.scale(bishop_black, SCALE_FACTOR)
    __image_white = pygame.transform.scale(bishop_white, SCALE_FACTOR)

    def __init__(self, position, team):
        Piece.__init__(self, position, team)

    def __repr__(self):
        return "b"

    def checkMove(self, position):
        return True

    def getPotentialMoves(self):
        self.potential_moves = {'xy': [],
                                '-xy': [],
                                'yx': [],
                                '-yx': []
                               }
        row = self._position.row
        col = self._position.col
        for i in range(7):
            self.potential_moves['xy'].append(Position(row + i, col + i))
            self.potential_moves['-yx'].append(Position(row + i, col - i))
            self.potential_moves['yx'].append(Position(row - i, col - i))
            self.potential_moves['-xy'].append(Position(row - i, col + i))

        return self.cropPotentialMoves()

    def getImage(self):
        if self._team == BLUE:
            return self.__image_black
        elif self._team == WHITE:
            return self.__image_white
        
class Rook(Piece):
    __image_black = pygame.transform.scale(rook_black, SCALE_FACTOR)
    __image_white = pygame.transform.scale(rook_white, SCALE_FACTOR)

    def __init__(self, position, team):
        Piece.__init__(self, position, team)

    def __repr__(self):
        return "r"

    def checkMove(self, position):
        return True
        Piece.__init__(self, position, team, board)

    def __repr__(self):
        return "r"

    def getPotentialMoves(self):
        self.potential_moves = {'x': [],
                                'y': [],
                                '-x': [],
                                '-y': []
                               }
        row = self._position.row
        col = self._position.col
        for i in range(8):
            self.potential_moves['x'].append(Position(row + i, col))
            self.potential_moves['-x'].append(Position(row - i, col))
            self.potential_moves['y'].append(Position(row, col - i))
            self.potential_moves['-y'].append(Position(row, col + i))

        return self.cropPotentialMoves()
        pass

    def getImage(self):
        if self._team == BLUE:
            return self.__image_black
        elif self._team == WHITE:
            return self.__image_white

class Queen(Piece):
    __image_black = pygame.transform.scale(queen_black, SCALE_FACTOR)
    __image_white = pygame.transform.scale(queen_white, SCALE_FACTOR)

    def __init__(self, position, team):
        Piece.__init__(self, position, team)

    def __repr__(self):
        return "q"

    def checkmove(self, position):
        return true

    def getPotentialMoves(self):
        Bishop.getPotentialMoves(self)
        Rook.getPotentialMoves(self)
        return self.cropPotentialMoves()

    def getImage(self):
        if self._team == BLUE:
            return self.__image_black
        elif self._team == WHITE:
            return self.__image_white
    
class King(Piece):
    __image_black = pygame.transform.scale(king_black, SCALE_FACTOR)
    __image_white = pygame.transform.scale(king_white, SCALE_FACTOR)

    def __init__(self, position, team):
        Piece.__init__(self, position, team)

    def __repr__(self):
        return "k"

    def checkMove(self, position):
        return True

    def getPotentialMoves(self):
        self.potential_moves['dummy'] = []
        row = self._position.row
        col = self._position.col
        self.potential_moves['dummy'].append(Position(row + 1, col))
        self.potential_moves['dummy'].append(Position(row - 1, col))
        self.potential_moves['dummy'].append(Position(row, col - 1))
        self.potential_moves['dummy'].append(Position(row, col + 1))

        self.potential_moves['dummy'].append(Position(row + 1, col + 1))
        self.potential_moves['dummy'].append(Position(row + 1, col - 1))
        self.potential_moves['dummy'].append(Position(row - 1, col - 1))
        self.potential_moves['dummy'].append(Position(row - 1, col + 1))

        return self.cropPotentialMoves()
        pass

    def getImage(self):
        if self._team == BLUE:
            return self.__image_black
        elif self._team == WHITE:
            return self.__image_white

class Pawn(Piece):
    __image_black = pygame.transform.scale(pawn_black, SCALE_FACTOR)
    __image_white = pygame.transform.scale(pawn_white, SCALE_FACTOR)

    def __init__(self, position, team):
        Piece.__init__(self, position, team)

    def __repr__(self):
        return "p"

    def checkMove(self, position):
        return True

    def getPotentialMoves(self):
        pass

    def getImage(self):
        if self._team == BLUE:
            return self.__image_black
        elif self._team == WHITE:
            return self.__image_white
