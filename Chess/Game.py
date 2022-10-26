import pygame
import time
import sys

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
bKnight = Piece('b', 'kn', 'b_knight.png')
wKnight = Piece('w', 'kn', 'w_knight.png')
wKnook = Piece('w', 'kno', 'w_knook.png')
bKnook = Piece('w', 'kno', 'b_knook.png')

