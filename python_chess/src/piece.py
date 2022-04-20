import pygame
import os
from abc import ABC, abstractmethod

from src.constants import SCALE_FACTOR, BLUE, WHITE, DEBUG, Position

knight_black = pygame.image.load("figures/black-knight.png")
knight_white = pygame.image.load("figures/white-knight.png")

DEBUG = False

'''
b_bishop = pygame.image.load(os.path.join("img", "black_bishop.png"))
b_king = pygame.image.load(os.path.join("img", "black_king.png"))
b_knight = pygame.image.load(os.path.join("img", "black_knight.png"))
b_pawn = pygame.image.load(os.path.join("img", "black_pawn.png"))
b_queen = pygame.image.load(os.path.join("img", "black_queen.png"))
b_rook = pygame.image.load(os.path.join("img", "black_rook.png"))

w_bishop = pygame.image.load(os.path.join("img", "white_bishop.png"))
w_king = pygame.image.load(os.path.join("img", "white_king.png"))
w_knight = pygame.image.load(os.path.join("img", "white_knight.png"))
w_pawn = pygame.image.load(os.path.join("img", "white_pawn.png"))
w_queen = pygame.image.load(os.path.join("img", "white_queen.png"))
w_rook = pygame.image.load(os.path.join("img", "white_rook.png"))

b = [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]
w = [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]

B = []
W = []

for img in b:
    B.append(pygame.transform.scale(img, (55, 55)))

for img in w:
    W.append(pygame.transform.scale(img, (55, 55)))
'''

class Piece(ABC):
    __image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    __image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)
    def __init__(self, position, team):
        self._team  = team
        self._old_position = (0,0)
        self._position = (0,0)
        self._potential_moves = []
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

    def getImage(self):
        if self._team == BLUE:
            return self.__image_black
        elif self._team == WHITE:
            return self.__image_white

class Knight(Piece):
    __image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    __image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, position, team):
        Piece.__init__(self, position, team)

    def __repr__(self):
        return "n"

    def getPotentialMoves(self):
        potential_moves = []
        self.__resetPotentialMoves()

        row = self._position.row
        col = self._position.col

        potential_moves.append(Position(row + 2, col + 1))
        potential_moves.append(Position(row + 1, col + 2))

        potential_moves.append(Position(row - 2, col + 1))
        potential_moves.append(Position(row - 1, col + 2))

        potential_moves.append(Position(row + 2, col - 1))
        potential_moves.append(Position(row + 1, col - 2))
        
        potential_moves.append(Position(row - 2, col - 1))
        potential_moves.append(Position(row - 1, col - 2))

        for move in potential_moves:
            if move.row > 7 or move.row < 0 or move.col > 7 or move.col < 0:
                continue
            else:
                self._potential_moves.append(move)

            if DEBUG:
                print(self.getPotentialMoves.__name__, self._potential_moves)
        return self._potential_moves

    def __resetPotentialMoves(self):
        self._potential_moves = []


class Bishop(Piece):
    __image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    __image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, position, team, board):
        Piece.__init__(self, position, team, board)

    def __repr__(self):
        return "b"

    def checkMove(self, position):
        return True

    def getPotentialMoves(self):
        pass
        
class Rook(Piece):
    __image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    __image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, position, team, board):
        Piece.__init__(self, position, team, board)

    def __repr__(self):
        return "r"

    def checkMove(self, position):
        return True
        Piece.__init__(self, position, team, board)

    def __repr__(self):
        return "r"

    def checkMove(self, position):
        return True
    
    def getPotentialMoves(self):
        pass

class Queen(Piece):
    __image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    __image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, position, team, board):
        Piece.__init__(self, position, team, board)

    def __repr__(self):
        return "q"

    def checkmove(self, position):
        return true

    def getPotentialMoves(self):
        pass
    
class King(Piece):
    __image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    __image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, position, team, board):
        Piece.__init__(self, position, team, board)

    def __repr__(self):
        return "k"

    def checkMove(self, position):
        return True

    def getPotentialMoves(self):
        pass

class Pawn(Piece):
    __image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    __image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, position, team, board):
        Piece.__init__(self, position, team, board)

    def __repr__(self):
        return "p"

    def checkMove(self, position):
        return True

    def getPotentialMoves(self):
        pass
