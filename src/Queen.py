from Piece import Piece
import pygame

class Queen(Piece):
    piece_type = "Queen"
    def __init__(self, color, row, col, size):
        self.color = color
        self.position = (row * size, col * size)
        if color == "Black":
            self.image_path = "../images/bQueen.png"
        else:
            self.image_path = "../images/wQueen.png"

        x_pixel, y_pixel = self.position
        super().__init__(color, size, x_pixel, y_pixel, self.image_path, row, col)
        # self.image_path = "../images/bQueen.png" if color == "black" else "../images/wQueen.png"

    def get_legal_moves(self, row, col):
        pass
