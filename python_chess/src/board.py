import pygame
import enum

import src.piece as p
from src.piece import Piece
from src.constants import SQUARE_SIZE, SCALE_FACTOR, WHITE, BLUE, ROWS, COLS, GREEN, DEBUG

#DEBUG = False

class Board:
    move = 0

    def __init__(self):
        self.createBoard()

    def getPiece(self, dest):
        #print(self.board[row][col])
        row = dest[0]
        col = dest[1]
        return self.board[row][col]

    def createBoard(self):
        self.board = []
        self.pieces = []
        self.turn = WHITE

        for row in range(ROWS):
            row = []
            for col in range(COLS):
                row.append(0)
            self.board.append(row)

        self.startingSetup()
        self.move += 1
        #self.printBoard()

    def changeTurns(self):
        if self.turn == WHITE:
            self.turn = BLUE
        else:
            self.turn = WHITE
        self.move += 1

    def placePiece(self, piece):
        row = piece.row
        col = piece.col
        self.board[row][col] = piece
        #print("placing piece on", (row, col))
        #self.printBoard()
        #if DEBUG:
            #print(self.placePiece.__name__, row, col, self.board[row][col])
    def resetValidMoves(self):
        self.valid_moves = []

    def removePiece(self, old_dest, new_dest):
        if isinstance(self.getPiece(new_dest), Piece):
            self.board[old_dest[0]][old_dest[1]] = 0
            print("removing Piece on", old_dest)

    def drawSquares(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BLUE, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def drawValidMoves(self, win):
        for move in self.valid_moves:
            print(move)
            row = SQUARE_SIZE * move[0] + SQUARE_SIZE//2
            col = SQUARE_SIZE * move[1] + SQUARE_SIZE//2
            pygame.draw.circle(win, GREEN, (col, row ), 15)
        #self.valid_moves = []

    def draw(self, win):
        for row in self.board:
            for tile in row:
                #if there is piece placed on tile so 
                if isinstance(tile, Piece):
                    piece = tile
                    row = SQUARE_SIZE * piece.row + (SQUARE_SIZE - SCALE_FACTOR[0]) / 2 
                    col = SQUARE_SIZE * piece.col + (SQUARE_SIZE - SCALE_FACTOR[0]) / 2 

                    win.blit(piece.getImage(), (col, row))
                else:
                    continue


    def startingSetup(self):
        #self.applcolFENposition("1N3/5/5/5/1n3")
        self.applcolFENposition("4N3/8/8/8/8/8/8/3n4")
        #self.applcolFENposition("RNBKQBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbkqbnr")


    def applcolFENposition(self, fen_string):
        row = 0
        col = 0
        for line in fen_string.split("/"):
            for char in line:
                try:
                    col += int(char)
                except ValueError:
                    self.initPieceInPosition(char, (row, col))
                    col+=1
            col = 0
            row+=1

    def initPieceInPosition(self, char, dest):
        if char.isupper():
            team = WHITE
        else:
            team = BLUE
        if char == "n" or char == "N":
            p.Knight(dest, team, self)
        elif char == "b" or char == "B":
            p.Bishop(dest, team, self)
        elif char == "r" or char == "R":
            p.Rook(dest, team, self)
        elif char == "q" or char == "Q":
            p.Queen(dest, team, self)
        elif char == "k" or char == "K":
            p.King(dest, team, self)
        elif char == "p" or char == "P":
            p.Pawn(dest, team, self)

    def printBoard(self):
        for row in self.board:
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
