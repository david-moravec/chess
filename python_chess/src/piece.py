import pygame
import os
from abc import ABC, abstractmethod

from src.constants import SCALE_FACTOR, BLUE, WHITE, DEBUG

knight_black = pygame.image.load("figures/black-knight.png")
knight_white = pygame.image.load("figures/white-knight.png")


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
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, dest, team, board):
        self.team  = team
        self.move(dest, board)
        self.olf_dest = (0,0)

    def move(self, dest, board):
        try: 
            board.valid_moves
            if dest in board.valid_moves:
                self.makeMove(dest)
                board.valid_moves = []
            else:
                self.makeMove(dest)
                pass
        except AttributeError:
                self.makeMove(dest)
        board.placePiece(self)


    def makeMove(self, dest):
        self.row = dest[0]
        self.col = dest[1]

        if DEBUG:
            print(self.makeMove.__name__, "movingPiece to", dest[0], dest[1])

    @abstractmethod
    def getValidMoves(self, board):
        pass

    def getImage(self):
        if self.team == BLUE:
            return self.image_black
        elif self.team == WHITE:
            return self.image_white

class Knight(Piece):
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, dest, team, board):
        Piece.__init__(self, dest, team, board)

    def __repr__(self):
        return "n"

    def getValidMoves(self, board):
        #print("getting valid moves")
        board.valid_moves = []
        potential_moves = []

        potential_moves.append((self.col + 2, self.row + 1))
        potential_moves.append((self.col + 1, self.row + 2))

        potential_moves.append((self.col - 2, self.row + 1))
        potential_moves.append((self.col - 1, self.row + 2))

        potential_moves.append((self.col + 2, self.row - 1))
        potential_moves.append((self.col + 1, self.row - 2))
        
        potential_moves.append((self.col + 2, self.row - 1))
        potential_moves.append((self.col + 1, self.row - 2))
        '''
        for d in range (-1, 2, 2):
            potential_moves.append((self.row + 2, self.col + d))
            potential_moves.append((self.row + d, self.col + 2))
        for d in range (-2, 4, 3):
            potential_moves.append((self.row + 1, self.col + d))
            potential_moves.append((self.row + d, self.col + 1))
        '''

        for move in potential_moves:
            row = move[0]
            col = move[1]
            dest = (row, col)
            try:
                target_piece = board.getPiece(dest)  
            except IndexError:
                continue

            #if target_piece.team == board.turn and target_piece != 0:
            board.valid_moves.append(move)
        #print(board.valid_moves)


class Bishop(Piece):
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, dest, team, board):
        Piece.__init__(self, dest, team, board)

    def __repr__(self):
        return "b"

    def checkMove(self, row, col):
        return True

    def getValidMoves(self, board):
        pass
        
class Rook(Piece):
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, dest, team, board):
        Piece.__init__(self, dest, team, board)

    def __repr__(self):
        return "r"

    def checkMove(self, row, col):
        return True
        Piece.__init__(self, row, col, team, board)

    def __repr__(self):
        return "r"

    def checkMove(self, row, col):
        return True
    
    def getValidMoves(self, board):
        pass

class Queen(Piece):
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, dest, team, board):
        Piece.__init__(self, dest, team, board)

    def __repr__(self):
        return "q"

    def checkmove(self, row, col):
        return true

    def getValidMoves(self, board):
        pass
    
class King(Piece):
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, dest, team, board):
        Piece.__init__(self, dest, team, board)

    def __repr__(self):
        return "k"

    def checkMove(self, row, col):
        return True

    def getValidMoves(self, board):
        pass

class Pawn(Piece):
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, dest, team, board):
        Piece.__init__(self, dest, team, board)

    def __repr__(self):
        return "p"

    def checkMove(self, row, col):
        return True

    def getValidMoves(self, board):
        pass
