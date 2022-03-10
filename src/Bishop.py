import Piece
import pygame

class Bishop(Piece.Piece):
    piece_type = "Bishop"
    def __init__(self, color, x, y, size):
        self.color = color
        self.position = (x * size, y * size)
        if color == "Black":
            self.image_path = "../images/bBishop.png"
        else:
            self.image_path = "../images/wBishop.png"
    
        x1, y1 = self.position
        super().__init__(color, size, x1, y1, self.image_path)
        # self.image_path = "../images/bBishop.png" if color == "black" else "../images/wBishop.png"

    def get_legal_moves(self, row, col):
        pass
