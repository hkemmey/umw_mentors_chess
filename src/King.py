import Piece
import pygame

class King(Piece.Piece):
    piece_type = "King"
    def __init__(self, color, row, col, size):
        self.color = color
        self.position = (row * size, col * size)
        if color == "Black":
            self.image_path = "../images/bKing.png"
        else:
            self.image_path = "../images/wKing.png"

        x_pixel, y_pixel = self.position
        super().__init__(color, size, x_pixel, y_pixel, self.image_path, row, col)
        # self.image_path = "../images/bKing.png" if color == "black" else "../images/wKing.png"

    def get_legal_moves(self, row, col):
        pass
