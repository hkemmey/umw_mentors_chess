from Piece import Piece
import pygame

class Queen(Piece):
    piece_type = "Queen"
    def __init__(self, color, x, y, size):
        self.color = color
        self.position = (x * size, y * size)
        if color == "black":
            self.image_path = "../images/bQueen.png"
        else:
            self.image_path = "../images/wQueen.png"

        x1, y1 = self.position
        super().__init__(color, size, x1, y1, self.image_path)
        # self.image_path = "../images/bQueen.png" if color == "black" else "../images/wQueen.png"

    def get_legal_moves(self, row, col):
        pass
