import Piece
import pygame

class Pawn(Piece.Piece):
    piece_type = "Pawn"
    def __init__(self, color):
        self.color = color

        if color == "black":
            self.image_path = "../images/bPawn.png"
        else:
            self.image_path = "../images/wPawn.png"
    
        # self.image_path = "../images/bPawn.png" if color == "black" else "../images/wPawn.png"

    def get_legal_moves(self, row, col):
        pass
