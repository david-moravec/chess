class Piece:
    def __init__(self, x, y, team, board):
        self.team  = team
        self.movePiece(x, y, board)

    def movePiece(self, new_x, new_y, board):
        self.makeMove(new_x, new_y)
        board.update(self)

    def makeMove(self, x, y):
        if self.checkMove(x, y) == True:
            self.x = x
            self.y = y

    def checkMove(self, x, y):
        pass

class Knight(Piece):
    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "n"

    def checkMove(self, x, y):
        return True

class Bishop(Piece):
    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "b"

    def checkMove(self, x, y):
        return True
        
class Rook(Piece):
    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "r"

    def checkMove(self, x, y):
        return True

class Queen(Piece):
    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "q"

    def checkMove(self, x, y):
        return True
    
class King(Piece):
    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "k"

    def checkMove(self, x, y):
        return True

class Pawn(Piece):
    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __repr__(self):
        return "p"

    def checkMove(self, x, y):
        return True
