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