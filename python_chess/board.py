import piece as p
import enum
from gui import GameBoard
from tkinter import Tk

class Board:
    def __init__(self):
        self.createBoard()
        self.game()

    def createBoard(self):
        self.tiles = []
        self.pieces = []

        for i in range(8):
            x = []
            for i in range(8):
                x.append(".")
            self.tiles.append(x)

        self.startingSetup()

    def startingSetup(self):
        self.applyFENposition("rnbkqbnr/ppppppp/8/8/8/8/pppppppp/rnbkqbnr")

    def game(self):
        root = Tk()
        chessBoard = GameBoard(root)
        chessBoard.placePieces(self.pieces, root)
        chessBoard.pack(side="top", fill="both", expand="true", padx=4, pady=4)
        root.mainloop()
        #while True:
            
    def movePiece(self):
        pass

    def update(self, piece):
        if (isinstance(piece.x, int)):
            x = piece.x
        else:
            x = TranslateAlgebraicNotation(piece.x)
        y = piece.y
        self.tiles[y][x] = piece

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
            self.pieces.append(p.Knight(x, y, "b", self))
        elif char == "b":
            self.pieces.append(p.Bishop(x, y, "b", self))
        elif char == "r":
            self.pieces.append(p.Rook(x, y, "b", self))
        elif char == "q":
            self.pieces.append(p.Queen(x, y, "b", self))
        elif char == "k":
            self.pieces.append(p.King(x, y, "b", self))
        elif char == "p":
            self.pieces.append(p.Pawn(x, y, "b", self))

        
        
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
