import pygame
import os

from src.constants import SCALE_FACTOR

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

class Piece:
    def __init__(self, x, y, team, board):
        self.team  = team
        self.movePiece(x, y, board)

    def movePiece(self, new_x, new_y, board):
        self.makeMove(new_x, new_y)
        board.placepiece(self)

    def makeMove(self, x, y):
        self.x = x
        self.y = y

    def getValidMoves(self, board):
        pass

class Knight(Piece):
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)


    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "n"

    def validMoves(self, board):
        valid_moves = []
        potential_moves = []
        for d in range (-1, 2, 2):
            potential_moves.append(tuple(self.x + 2, self.y + d))
            potential_moves.append(tuple(self.x + d, self.y + 2))
        for d in range (-2, 4, 3):
            potential_moves.append(tuple(self.x + 1, self.y + d))
            potential_moves.append(tuple(self.x + d, self.y + 1))

        for move in potential_moves:
            x = move[0]
            y = move[1]
            target_piece = board.getPiece(x, y)  

            if target_piece != board.turn or target_piece == 0:
                valid_moves.append(move)
        return valid_moves


class Bishop(Piece):
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "b"

    def checkMove(self, x, y):
        return True
        
class Rook(Piece):
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "r"

    def checkMove(self, x, y):
        return True

class Queen(Piece):
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "q"

    def checkMove(self, x, y):
        return True
    
class King(Piece):
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "k"

    def checkMove(self, x, y):
        return True

class Pawn(Piece):
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "p"

    def checkMove(self, x, y):
        return True
