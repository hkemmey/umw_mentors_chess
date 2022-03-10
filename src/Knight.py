import Piece
import pygame

class Knight(Piece.Piece):
    piece_type = "Knight"
    def __init__(self, color, x, y, size):
        self.color = color
        self.position = (x * size, y * size)
        if color == "Black":
            self.image_path = "../images/bKnight.png"
        else:
            self.image_path = "../images/wKnight.png"

        x1, y1 = self.position
        super().__init__(color, size, x1, y1, self.image_path)
        # self.image_path = "../images/bKnight.png" if color == "black" else "../images/wKnight.png"

    def get_legal_moves(self, row, col):
        pass
