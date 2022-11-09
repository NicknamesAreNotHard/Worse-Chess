import pygame
import time
import sys
import os
print(os.getcwd())
board = [['  ' for i in range(8)] for i in range(8)]


## Creates a chess piece class that shows what team a piece is on,
# what type of piece it is and whether or not it can be killed by another selected piece.
class Piece:
    def __init__(self, team, type, image, killable=False):
        self.team = team
        self.type = type
        self.killable = killable
        self.image = image

bPawn = Piece('b', 'p', 'b_pawn.png')
wPawn = Piece('w', 'p', 'w_pawn.png')
bKing = Piece('b', 'k', 'b_king.png')
wKing = Piece('w', 'k', 'w_king.png')
bRook = Piece('b', 'r', 'b_rook.png')
wRook = Piece('w', 'r', 'w_rook.png')
bBishop = Piece('b', 'b', 'b_bishop.png')
wBishop = Piece('w', 'b', 'w_bishop.png')
bQueen = Piece('b', 'q', 'b_queen.png')
wQueen = Piece('w', 'q', 'w_queen.png')
bRat = Piece('b', 'ra', 'b_rat.png')
wRat = Piece('w', 'ra', 'w_rat.png')
wKnook = Piece('w', 'kno', 'w_knook.png')
bKnook = Piece('w', 'kno', 'b_knook.png')

starting_order = {(0, 0): pygame.image.load(bRook.image), (1, 0): pygame.image.load(bRat.image),
                  (2, 0): pygame.image.load(bBishop.image), (3, 0): pygame.image.load(bKing.image),
                  (4, 0): pygame.image.load(bQueen.image), (5, 0): pygame.image.load(bBishop.image),
                  (6, 0): pygame.image.load(bRat.image), (7, 0): pygame.image.load(bRook.image),
                  (0, 1): pygame.image.load(bPawn.image), (1, 1): pygame.image.load(bPawn.image),
                  (2, 1): pygame.image.load(bPawn.image), (3, 1): pygame.image.load(bPawn.image),
                  (4, 1): pygame.image.load(bPawn.image), (5, 1): pygame.image.load(bPawn.image),
                  (6, 1): pygame.image.load(bPawn.image), (7, 1): pygame.image.load(bPawn.image), 
                  (2, 2): pygame.image.load(bRat.image), (5, 2): pygame.image.load(bRat.image),

                  (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
                  (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,
                  (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
                  (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,
                  (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
                  (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,
                  (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
                  (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,

                  (0, 6): pygame.image.load(wPawn.image), (1, 6): pygame.image.load(wPawn.image),
                  (2, 6): pygame.image.load(wPawn.image), (3, 6): pygame.image.load(wPawn.image),
                  (4, 6): pygame.image.load(wPawn.image), (5, 6): pygame.image.load(wPawn.image),
                  (6, 6): pygame.image.load(wPawn.image), (7, 6): pygame.image.load(wPawn.image),
                  (0, 7): pygame.image.load(wRook.image), (1, 7): pygame.image.load(wRat.image),
                  (2, 7): pygame.image.load(wBishop.image), (3, 7): pygame.image.load(wKing.image),
                  (4, 7): pygame.image.load(wQueen.image), (5, 7): pygame.image.load(wBishop.image),
                  (6, 7): pygame.image.load(wRat.image), (7, 7): pygame.image.load(wFrog.image),}

def create_board(board):
    board[0] = [Piece('b', 'r', 'b_rook.png'), Piece('b', 'kn', 'b_rat.png'), Piece('b', 'b', 'b_bishop.png'), \
               Piece('b', 'q', 'b_queen.png'), Piece('b', 'k', 'b_king.png'), Piece('b', 'b', 'b_bishop.png'), \
               Piece('b', 'kn', 'b_rat.png'), Piece('b', 'r', 'b_rook.png'), Piece("b","ra","b_rat.png" )]

    board[7] = [Piece('w', 'r', 'w_rook.png'), Piece('w', 'kn', 'w_rat.png'), Piece('w', 'b', 'w_bishop.png'), \
               Piece('w', 'q', 'w_queen.png'), Piece('w', 'k', 'w_king.png'), Piece('w', 'b', 'w_bishop.png'), \
               Piece('w', 'kn', 'w_rat.png'), Piece('w', 'r', 'w_rook.png'), Piece("w","ra","w_rat.png" )]    
    for i in range(8):
        board[1][i] = Piece('b', 'p', 'b_pawn.png')
        board[6][i] = Piece('w', 'p', 'w_pawn.png')
    return board

    ## returns the input if the input is within the boundaries of the board
def on_board(position):
    if position[0] > -1 and position[1] > -1 and position[0] < 8 and position[1] < 8:
        return True