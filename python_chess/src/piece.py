import pygame
import os
from abc import ABC, abstractmethod

from src.constants import SCALE_FACTOR, BLUE, WHITE, DEBUG

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
        self.__old_position = (0,0)
        self.__valid_moves = []
        self.move(position, init=True)
        self.__moved = False
        self.alive = True

    def position(self):
        return (self._position)

    def oldPosition(self):
        return self.__old_position

    def team(self):
        return self._team

    def move(self, position, init=False):
        # if we have the first round of chess we dont have any valid moves to look for 
        #import pdb; pdb.set_trace()
        try: 
            if DEBUG:
                print(self.__valid_moves, position)

            if position in self.__valid_moves or init:
                self._position = position
                self.__moved = True
                self.__resetValidMoves()
            else:
                pass
            if DEBUG:
                print(board.valid_moves)
        except AttributeError:
                pass
                #self.makeMove(position)

        # remove piece from old colation

    def resetMoved(self):
        self.moved = False

    def didMove(self, position):
        print(position, self.oldPosition())
        return position != self.oldPosition()

    def resetValidMoves(self):
        self.valid_moves = []

    @abstractmethod
    def getValidMoves(self, board):
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

    def getValidMoves(self, board):
        #print(self.row, self.col)
        potential_moves = []

        potential_moves.append((self.row + 2, self.col + 1))
        potential_moves.append((self.row + 1, self.col + 2))

        potential_moves.append((self.row - 2, self.col + 1))
        potential_moves.append((self.row - 1, self.col + 2))

        potential_moves.append((self.row + 2, self.col - 1))
        potential_moves.append((self.row + 1, self.col - 2))
        
        potential_moves.append((self.row - 2, self.col - 1))
        potential_moves.append((self.row - 1, self.col - 2))
        '''
        for d in range (-1, 2, 2):
            potential_moves.append((self.col + 2, self.col + d))
            potential_moves.append((self.col + d, self.col + 2))
        for d in range (-2, 4, 3):
            potential_moves.append((self.col + 1, self.col + d))
            potential_moves.append((self.col + d, self.col + 1))
        '''

        for move in potential_moves:
            if move[0] > 7 or move[0] < 0 or move[1] > 7 or move[1] < 0:
                continue

            position = move
            try:
                target_piece = board.getPiece(position)  
            except IndexError:
                continue

            #if target_piece.team == board.turn and target_piece != 0:
            self.__valid_moves.append

            if DEBUG:
                print(self.getValidMoves.__name__, valid_moves)
        #print(board.valid_moves)


class Bishop(Piece):
    __image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    __image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, position, team, board):
        Piece.__init__(self, position, team, board)

    def __repr__(self):
        return "b"

    def checkMove(self, position):
        return True

    def getValidMoves(self, board):
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
    
    def getValidMoves(self, board):
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

    def getValidMoves(self, board):
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

    def getValidMoves(self, board):
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

    def getValidMoves(self, board):
        pass
