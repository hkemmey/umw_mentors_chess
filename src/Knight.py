import Piece
import pygame

class Knight(Piece.Piece):
    piece_type = "Knight"
    def __init__(self, color):
        self.color = color

        if color == "black":
            self.image_path = "../images/bKnight.png"
        else:
            self.image_path = "../images/wKnight.png"
    
        # self.image_path = "../images/bKnight.png" if color == "black" else "../images/wKnight.png"

    def get_legal_moves(self, row, col):
        pass
