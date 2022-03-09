import Piece
import pygame

class King(Piece.Piece):
    piece_type = "King"
    def __init__(self, color, x, y, size):
        self.color = color
        self.position = (x * size, y * size)
        if color == "black":
            self.image_path = "../images/bKing.png"
        else:
            self.image_path = "../images/wKing.png"

        x1, y1 = self.position
        super().__init__(color, size, x1, y1, self.image_path)
        # self.image_path = "../images/bKing.png" if color == "black" else "../images/wKing.png"

    def get_legal_moves(self, row, col):
        pass
