import piece as p
import enum
import tkinter as tk
from gui import GameBoard

class Board:
    def __init__(self):
        self.createBoard()
        #self.game()

    def createBoard(self):
        self.pieces = []
        self.startingSetup()

    def startingSetup(self):
        self.applyFENposition("rnbkqbnr/ppppppp/8/8/8/8/pppppppp/rnbkqbnr")

    def game(self):
        root = tk.Tk()
        chessBoard = GameBoard(root)
        chessBoard.update(self.pieces)
        while True:
            
            
    def movePiece(self):
        pass

    def update(self, piece):
        self.pieces.append(piece)

    def applyFENposition(self, fen_string):
        x = 0
        y = 0
        for line in fen_string.split("/"):
            for char in line:
                try:
                    x += int(char)
                except ValueError:
                    self.initPieceInPosition(char, x, y)
                    x+=1
            x = 0
            y+=1

    def initPieceInPosition(self, char, x, y):
        if char == "n":
            p.Knight(x, y, char, self)
        elif char == "b":
            p.Bishop(x, y, char, self)
        elif char == "r":
            p.Rook(x, y, char, self)
        elif char == "q":
            p.Queen(x, y, char, self)
        elif char == "k":
            p.King(x, y, char, self)
        elif char == "p":
            p.Pawn(x, y, char, self)

        
        
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
