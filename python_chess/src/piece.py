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

    def validMoves(self, x, y):
        pass

class Knight(Piece):
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
