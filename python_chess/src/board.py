import pygame
import enum

import src.piece as p
from src.piece import Piece
from src.constants import SQUARE_SIZE, SCALE_FACTOR, WHITE, BLUE, ROWS, COLS, GREEN, DEBUG, Position

#stores all the info about pices passes moves from pygame guie to selected piece

#DEBUG = False
class Tile:
    def __init__(self, position):
        self.__piece
        self.position = position

    def getPiece():
        return self.__piece

    def addPiece(piece):
        self.pieces = self.pieces + (piece)

class Board:
    #__chessSet
    def __init__(self):
        self.__createBoard()

    def getMoveNumber(self):
        return self.__move

    def _update(self):
        self.__drawSquares(self.win)
        self.__drawPieces(self.win)
        try:
            self.__board.drawValidMoves(self.win)
        except:
            pass

    def _getPiece(self, position):
        return self.__board[position.row][position.col]

    def __createBoard(self):
        self.__board = []
        self.__pieces = ()
        self.turn = WHITE

        for row in range(ROWS):
            row = []
            for col in range(COLS):
                row.append(0)
            self.__board.append(row)

        self.__startingSetup()

        #self.printBoard()


    def __placePiece(self, piece):
        row = piece.row
        col = piece.col
        self.__board[row][col] = piece
        #print("placing piece on", (row, col))
        #self.printBoard()
        #if DEBUG:
            #print(self.placePiece.__name__, row, col, self.board[row][col])


    def __removePiece(self, old_dest, new_dest):
        if isinstance(self.getPiece(new_dest), Piece):
            self.board[old_dest[0]][old_dest[1]] = 0
            if DEBUG:
                print("removing Piece on", old_dest)

    def __drawSquares(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BLUE, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def __drawValidMoves(self, win):
        for move in self.valid_moves:
            #print(move)
            row = SQUARE_SIZE * move[0] + SQUARE_SIZE//2
            col = SQUARE_SIZE * move[1] + SQUARE_SIZE//2
            pygame.draw.circle(win, GREEN, (col, row ), 15)
        #self.valid_moves = []

    def __drawPieces(self, win):
        for piece in self.__pieces:
            if piece.alive:
                square_center = SQUARE_SIZE * piece.position().row + (SQUARE_SIZE - SCALE_FACTOR[0]) / 2 
                win.blit(piece.getImage(), square_center)
                print("kek")
            else:
                continue


    def __startingSetup(self):
        #self.__applcolFENposition("1N3/5/5/5/1n3")
        #self.__applcolFENposition("4N3/pppppppp/8/8/8/8/pppppppp/3n4")
        self.__applcolFENposition("4N3/8/8/8/8/8/8/3n4")
        #print(self.__piecesposition())
        #self.__applcolFENposition("RNBKQBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbkqbnr")


    def __applcolFENposition(self, fen_string):
        row = 0
        col = 0
        for line in fen_string.split("/"):
            for char in line:
                try:
                    col += int(char)
                except ValueError:
                    self.__initPieceInPosition(char, (row, col))
                    col+=1
            col = 0
            row+=1

    def __initPieceInPosition(self, char, dest):
        if char.isupper():
            team = WHITE
        else:
            team = BLUE
        if char == "n" or char == "N":
            piece = p.Knight(dest, team, self)
        elif char == "b" or char == "B":
            piece = p.Bishop(dest, team, self)
        elif char == "r" or char == "R":
            piece = p.Rook(dest, team, self)
        elif char == "q" or char == "Q":
            piece = p.Queen(dest, team, self)
        elif char == "k" or char == "K":
            piece = p.King(dest, team, self)
        elif char == "p" or char == "P":
            piece = p.Pawn(dest, team, self)

        self.__pieces = self.__pieces + (piece,)

    def printBoard(self):
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
