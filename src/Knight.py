import Piece
import pygame

class Knight(Piece.Piece):
    piece_type = "Knight"
    def __init__(self, color, row, col, size):
        self.color = color
        self.position = (row * size, col * size)
        if color == "Black":
            self.image_path = "../images/bKnight.png"
        else:
            self.image_path = "../images/wKnight.png"

        x_pixel, y_pixel = self.position
        super().__init__(color, size, x_pixel, y_pixel, self.image_path, row, col)
        # self.image_path = "../images/bKnight.png" if color == "black" else "../images/wKnight.png"

    def get_legal_moves(self, row, col):
        pass
