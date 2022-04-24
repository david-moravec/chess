import pygame
import enum

import src.piece as p
from src.piece import Piece
from src.constants import SQUARE_SIZE, SCALE_FACTOR, WHITE, BLUE, ROWS, COLS, GREEN, DEBUG, Position

#stores all the info about pices passes moves from pygame guie to selected piece

#DEBUG = False

class Board:
    def __init__(self):
        self.__createBoard()

    def getMoveNumber(self):
        return self.__move

    def _update(self):
        self.__drawSquares(self.win)
        self.__drawPieces(self.win)
        try:
            self.__drawValidMoves(self.win)
        except:
            pass

    def _getPiece(self, position):
        return self.__board[position.row][position.col]

    def __createBoard(self):
        self.__board = []
        self._pieces = ()
        self._pieces_alive = []
        self.turn = WHITE

        for row in range(ROWS):
            row = []
            for col in range(COLS):
                row.append(0)
            self.__board.append(row)

        self.__startingSetup()
        self._valid_moves = []


    def _getValidMoves(self, piece):
        for move in piece.getPotentialMoves():
            target = self._getPiece(move)
            if (type(target) == type(Piece)):
                if (target.team() == piece.team()):
                    pass
            else:
                self._valid_moves.append(move)


    def __drawSquares(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BLUE, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def _updateLivingPieces(self):
        for piece in self._pieces_alive:
            if not piece.alive:
                self._pieces_alive.pop(piece)

    def __drawValidMoves(self, win):
        for move in self._valid_moves:
            row = SQUARE_SIZE * move[1] + SQUARE_SIZE//2
            col = SQUARE_SIZE * move[0] + SQUARE_SIZE//2
            pygame.draw.circle(win, GREEN, (row, col), 15)

    def __drawPieces(self, win):
        for piece in self._pieces:
            if piece.alive:
                square_center = tuple(SQUARE_SIZE * coord + (SQUARE_SIZE - SCALE_FACTOR[0]) / 2 for coord in piece.position()) 
                square_center_cor = Position(row=square_center[1], col=square_center[0])
                win.blit(piece.getImage(), square_center_cor)
            else:
                continue

    def _resetValidMoves(self):
        self._valid_moves = []


    def __startingSetup(self):
        #self.__applcolFENposition("1N3/5/5/5/1n3")
        #self.__applcolFENposition("4N3/pppppppp/8/8/8/8/pppppppp/3n4")
        self.__applcolFENposition("3BN3/8/8/8/8/8/8/3nb3")
        #print(self._piecesposition())
        #self.__applcolFENposition("RNBKQBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbkqbnr")


    def __applcolFENposition(self, fen_string):
        row = 0
        col = 0
        for line in fen_string.split("/"):
            for char in line:
                try:
                    col += int(char)
                except ValueError:
                    self.__initPieceInPosition(char, Position(row, col))
                    col+=1
            col = 0
            row+=1

    def __initPieceInPosition(self, char, position):
        if char.isupper():
            team = WHITE
        else:
            team = BLUE
        if char == "n" or char == "N":
            piece = p.Knight(position, team)
        elif char == "b" or char == "B":
            piece = p.Bishop(position, team)
        elif char == "r" or char == "R":
            piece = p.Rook(position, team)
        elif char == "q" or char == "Q":
            piece = p.Queen(position, team)
        elif char == "k" or char == "K":
            piece = p.King(position, team)
        elif char == "p" or char == "P":
            piece = p.Pawn(position, team)

        self._pieces = self._pieces + (piece,)
        self._pieces_alive.append(piece)

    def _printBoard(self):
        for row in self.__board:
            print(row)
        print("\n")    


        
        
def TranslateAlgebraicNotation(row):
    try:
        row = AlgebraicNotationDict[row]
        return row.value
    except:
        row = AlgebraicNotation(row)
        for key in AlgebraicNotationDict.keys():
            if row == AlgebraicNotationDict[key]:
                return key

class AlgebraicNotation(enum.Enum):
    a = 0 
    b = 1 
    c = 2 
    d = 3 
    e = 4 
    f = 5 
    g = 6 
    h = 7 

AlgebraicNotationDict = {
    "a" : AlgebraicNotation.a, 
    "b" : AlgebraicNotation.b, 
    "c" : AlgebraicNotation.c, 
    "d" : AlgebraicNotation.d, 
    "e" : AlgebraicNotation.e, 
    "f" : AlgebraicNotation.f, 
    "g" : AlgebraicNotation.g, 
    "h" : AlgebraicNotation.h 
    } 
