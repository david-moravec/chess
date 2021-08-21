import pygame
import enum
import src.piece as p
from src.constants import SQUARE_SIZE, WHITE, BLUE, ROWS, COLS

class Board:
    def __init__(self):
        self.createBoard()

    def getPiece(self, x, y):
        #print(self.board[x][y])
        return self.board[x][y]

    def createBoard(self):
        self.board = []
        self.pieces = []
        self.turn = WHITE

        for i in range(ROWS):
            x = []
            for i in range(8):
                x.append(0)
            self.board.append(x)

        self.startingSetup()

    def placepiece(self, piece):
        if (isinstance(piece.x, int)):
            x = piece.x
        else:
            x = TranslateAlgebraicNotation(piece.x)
        y = piece.y
        self.board[x][y] = piece

    def draw_squares(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BLUE, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def startingSetup(self):
        self.applyFENposition("RNBKQBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbkqbnr")


    def applyFENposition(self, fen_string):
        x = 0
        y = 0
        for line in fen_string.split("/"):
            for char in line:
                try:
                    y += int(char)
                except ValueError:
                    self.initPieceInPosition(char, x, y)
                    y+=1
            y = 0
            x+=1

    def initPieceInPosition(self, char, x, y):
        if char.isupper():
            team = WHITE
        else:
            team = BLUE

        if char == "n" or char == "N":
            p.Knight(x, y, team, self)
        elif char == "b" or char == "B":
            p.Bishop(x, y, team, self)
        elif char == "r" or char == "R":
            p.Rook(x, y, team, self)
        elif char == "q" or char == "Q":
            p.Queen(x, y, team, self)
        elif char == "k" or char == "K":
            p.King(x, y, team, self)
        elif char == "p" or char == "P":
            p.Pawn(x, y, team, self)

        
        
def TranslateAlgebraicNotation(x):
    try:
        x = AlgebraicNotationDict[x]
        return x.value
    except:
        x = AlgebraicNotation(x)
        for key in AlgebraicNotationDict.keys():
            if x == AlgebraicNotationDict[key]:
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
