import Piece
import pygame

class Rook(Piece.Piece):
    piece_type = "Rook"
    def __init__(self, color):
        super().__init__(color)
        self.color = color

        if color == "black":
            self.image_path = "../images/bRook.png"
        else:
            self.image_path = "../images/wRook.png"
    
        # self.image_path = "../images/bRook.png" if color == "black" else "../images/wRook.png"

    def get_legal_moves(self, row, col):
        pass

