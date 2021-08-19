from PIL import Image
from PIL import ImageTk

class Piece:
    def __init__(self, x, y, name, board):
        self.name  = name
        self.killable = False
        self.guarded = False
        self.movePiece(x, y, board)

    def movePiece(self, new_x, new_y, board):
        self.makeMove(new_x, new_y, board)
        board.update(self)

    def makeMove(self, x, y, board):
        if self.checkMove(x, y, board) == True:
            self.x = x
            self.y = y

    def checkMove(self, x, y, board):
        pass

class Knight(Piece):
    image_path = 'figures/white-knight.ppm'
    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "n"

    def checkMove(self, x, y, board):
        for x in range(-2, 2, 4):
            for y in range(-2, 2, 4):
                return True
        return True

class Bishop(Piece):
    image_path = 'figures/white-knight.ppm'
    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "b"

    def checkMove(self, x, y, board):
        return True
        
class Rook(Piece):
    image_path = 'figures/white-knight.ppm'
    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "r"

    def checkMove(self, x, y, board):
        return True

class Queen(Piece):
    image_path = 'figures/white-knight.ppm'
    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "q"

    def checkMove(self, x, y, board):
        return True
    
class King(Piece):
    image_path = 'figures/white-knight.ppm'
    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "k"

    def checkMove(self, x, y, board):
        return True

class Pawn(Piece):
    image_path = r'figures/white-knight.ppm'
    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "p"

    def checkMove(self, x, y, board):
        return True
