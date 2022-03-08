import Piece
import pygame

class Bishop(Piece.Piece):
    piece_type = "Bishop"
    def __init__(self, color):
        self.color = color

        if color == "black":
            self.image_path = "../images/bBishop.png"
        else:
            self.image_path = "../images/wBishop.png"
    
        # self.image_path = "../images/bBishop.png" if color == "black" else "../images/wBishop.png"

    def get_legal_moves(self, row, col):
        pass
