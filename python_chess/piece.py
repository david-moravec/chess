class Knight:
    def __init__(self, x, y, team, board):
        self.team  = team
        self.move(x, y, board)

    def __str__(self):
        return "k"

    def move(self, new_x, new_y, board):
        if self.checkMove() == True:
            self.x = new_x
            self.y = new_y
            board.update(self)

    def checkMove(self):
        return True
        
