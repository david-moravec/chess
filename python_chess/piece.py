class Piece:
    def __init__(self, x, y, team, board):
        self.team  = team
        self.movePiece(x, y, board)

    def movePiece(self, new_x, new_y, board):
        self.makeMove(new_x, new_y)
        self.updateBoard(board)

    def makeMove(self, x, y):
        if self.checkMove(x, y) == True:
            self.x = x
            self.y = y

    def updateBoard(self, board):
        board.update(self)

    def checkMove(self, x, y):
        pass

class Knight(Piece):
    def __init__(self, x, y, team, board):
        Piece.__init__(self, x, y, team, board)

    def __str__(self):
        return "k"

    def checkMove(self, x, y):
        return True
        
