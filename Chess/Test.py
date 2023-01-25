import pygame
import tkinter as tk
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
bRat = Piece('b', 'kn', 'b_rat.png')
wRat = Piece('w', 'kn', 'w_rat.png')
wKnook = Piece('w', 'kno', 'w_knook.png')
bKnook = Piece('w', 'kno', 'b_knook.png')
wFrog = Piece("w", "f", "w_frog.png")
bFrog = Piece("b", "f", "b_frog.png")

window = tk.Tk()

# Set the window title
window.title("Interactive Chess Board")

# Create a canvas to hold the board
canvas = tk.Canvas(window, width=400, height=400)

# Draw the board using squares of alternating colors
for row in range(8):
  for col in range(8):
    if (row + col) % 2 == 0:
      color = "black"
    else:
      color = "white"
    canvas.create_rectangle(row * 50, col * 50, (row + 1) * 50, (col + 1) * 50, fill=color)
    
print(row + col)

# Set up an event handler to respond to clicks on the board
def handle_click(event):
  print(f"Clicked at: ({event.x}, {event.y})")

canvas.bind("<Button-1>", handle_click)

# Pack the canvas into the window and show the window
canvas.pack()
window.mainloop()