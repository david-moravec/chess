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
    def __init__(self, dest, team, board):
        self.team  = team
        self.move(dest, board)

    def move(self, dest, board):
        try: 
            board.valid_moves
            if dest in board.valid_moves:
                self.makeMove(dest)
                board.valid_moves = []
        except AttributeError:
                self.makeMove(dest)

        board.placePiece(self)

    def makeMove(self, dest):
        self.row = dest[0]
        self.col = dest[1]

    def getValidMoves(self, board):
        pass

class Knight(Piece):
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, dest, team, board):
        Piece.__init__(self, dest, team, board)

    def __repr__(self):
        return "n"

    def getValidMoves(self, board):
        board.valid_moves = []
        potential_moves = []
        for d in range (-1, 2, 2):
            potential_moves.append((self.row + 2, self.col + d))
            potential_moves.append((self.row + d, self.col + 2))
        for d in range (-2, 4, 3):
            potential_moves.append((self.row + 1, self.col + d))
            potential_moves.append((self.row + d, self.col + 1))

        for move in potential_moves:
            row = move[0]
            col = move[1]
            try:
                target_piece = board.getPiece(row, col)  
            except IndexError:
                continue

            if target_piece.team == board.turn and target_piece != 0:
                board.valid_moves.append(move)

class Bishop(Piece):
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, dest, team, board):
        Piece.__init__(self, dest, team, board)

    def __repr__(self):
        return "b"

    def checkMove(self, row, col):
        return True
        
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

class Queen(Piece):
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, dest, team, board):
        Piece.__init__(self, dest, team, board)

    def __repr__(self):
        return "q"

    def checkmove(self, row, col):
        return true
    
class King(Piece):
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, dest, team, board):
        Piece.__init__(self, dest, team, board)

    def __repr__(self):
        return "k"

    def checkMove(self, row, col):
        return True

class Pawn(Piece):
    image_black = pygame.transform.scale(knight_black, SCALE_FACTOR)
    image_white = pygame.transform.scale(knight_white, SCALE_FACTOR)

    def __init__(self, dest, team, board):
        Piece.__init__(self, dest, team, board)

    def __repr__(self):
        return "p"

    def checkMove(self, row, col):
        return True
