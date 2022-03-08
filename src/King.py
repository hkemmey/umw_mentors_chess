import Piece
import pygame

class King(Piece.Piece):
    piece_type = "King"
    def __init__(self, color):
        self.color = color

        if color == "black":
            self.image_path = "../images/bKing.png"
        else:
            self.image_path = "../images/wKing.png"
    
        # self.image_path = "../images/bKing.png" if color == "black" else "../images/wKing.png"

    def get_legal_moves(self, row, col):
        pass
