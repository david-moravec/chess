import piece as p
import enum

class Board:
    def __init__(self):
        self.createBoard()

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
       self.pieces.append(p.Knight('g', 0, 'b', self))

    def update(self, piece):
        x = TranslateAlgebraicNotation(piece.x)
        y = piece.y
        self.tiles[x][y] = piece
        
def TranslateAlgebraicNotation(x):
    try:
        coord = AlgebraicNotationDict[x]
        return coord.value
    except:
        coord = AlgebraicNotation(x)
        for key in AlgebraicNotationDict.keys():
            if coord == AlgebraicNotationDict[key]:
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
